import time
import tracemalloc
import csv
import random

from priority_queue import DijkstraMinHeap
from dijkstra import pq_dijkstra, arr_dijkstra
from graph_utils import add_adj_list_edge, print_adj_list
from graph_utils import add_adj_mat_edge, print_adj_mat

class GraphBenchmarker:
    def __init__(self):
        # Input sizes defined in Section 6.1 
        self.vertices_sizes = [100, 500, 1000, 2000, 5000]
        self.trials = 5

    def generate_test_data(self, v, density_type):
        """Generates vertices and edges based on density categories."""
        nodes = {str(i) for i in range(v)}
        edges = []
        
        if density_type == 'Sparse':
            e_target = 2 * v
        elif density_type == 'Medium':
            e_target = int(v * (v ** 0.5))
        else: # Dense
            e_target = int(0.5 * v * (v - 1) / 2)
            
        max_edges = int(v * (v - 1) / 2)
        e_target = min(e_target, max_edges)
        
        # Optimization to prevent hanging on dense graph generation
        if e_target > max_edges * 0.8: 
            all_pairs = [(str(i), str(j)) for i in range(v) for j in range(i+1, v)]
            selected_pairs = random.sample(all_pairs, e_target)
            for u, dest in selected_pairs:
                edges.append((u, dest, random.randint(1, 100)))
        else:
            existing_edges = set()
            nodes_list = list(nodes)
            while len(edges) < e_target:
                u, dest = random.sample(nodes_list, 2)
                if u > dest: u, dest = dest, u # normalize pair to undirected
                
                if (u, dest) not in existing_edges:
                    existing_edges.add((u, dest))
                    edges.append((u, dest, random.randint(1, 100)))
                    
        return nodes, edges

    def measure_execution(self, func, *args):
        """Measures average runtime over 5 trials and peak memory usage."""
        runtimes = []
        peak_memory = 0

        for _ in range(self.trials):
            tracemalloc.start()
            start_time = time.perf_counter()
            
            # Execute the algorithm
            result = func(*args)
            
            end_time = time.perf_counter()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            runtimes.append((end_time - start_time) * 1000) # Convert to ms
            peak_memory = max(peak_memory, peak)

        avg_time = sum(runtimes) / self.trials
        peak_memory_mb = peak_memory / (1024 * 1024) # Convert to MB
        
        return result, avg_time, peak_memory_mb

    def verify_correctness(self, dist_a, dist_b):
        """Verifies both implementations produced the same shortest path distances."""
        return dist_a == dist_b

    def run_benchmarks(self):
        """Main execution loop for all required experiments."""
        print(f"{'Graph Type':<15} | {'#Vertices':<10} | {'Method':<25} | {'Time (ms)':<10} | {'Memory (MB)':<12} | {'Correct'}")
        print("-" * 90)

        densities = ['Sparse', 'Medium', 'Dense']

        # Open the CSV file for writing
        with open('benchmark_results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the CSV header expected by the R script
            writer.writerow(['Density', 'Vertices', 'Method', 'Time_ms', 'Memory_MB'])

            for v in self.vertices_sizes:
                for density in densities:
                    # 1. Generate Graph Data
                    nodes, edges = self.generate_test_data(v, density)
                    graph_name = f"{density}-{v}"
                    
                    # 2. Build Adjacency Structures
                    adj_list, node_index = add_adj_list_edge(nodes, edges)
                    adj_mat, _ = add_adj_mat_edge(nodes, edges)
                    
                    src_node = sorted(list(nodes))[0]
                    src_idx = node_index[src_node]
                    
                    # 3. Benchmark Priority Queue (Adjacency List)
                    pq_result, pq_time, pq_mem = self.measure_execution(pq_dijkstra, adj_list, v, src_idx)
                    print(f"{graph_name:<15} | {v:<10} | {'Heap (Adj List)':<25} | {pq_time:<10.4f} | {pq_mem:<12.4f} | {'N/A'}")
                    writer.writerow([density, v, 'Heap(AdjList)', round(pq_time, 4), round(pq_mem, 4)])

                    # 4. Benchmark Array (Adjacency List)
                    arr_list_result, arr_list_time, arr_list_mem = self.measure_execution(arr_dijkstra, adj_list, 'l', v, src_idx)
                    is_correct_list = self.verify_correctness(pq_result[0], arr_list_result[0])
                    print(f"{graph_name:<15} | {v:<10} | {'Array (Adj List)':<25} | {arr_list_time:<10.4f} | {arr_list_mem:<12.4f} | {is_correct_list}")
                    writer.writerow([density, v, 'Array(AdjList)', round(arr_list_time, 4), round(arr_list_mem, 4)])

                    # 5. Benchmark Array (Adjacency Matrix)
                    arr_mat_result, arr_mat_time, arr_mat_mem = self.measure_execution(arr_dijkstra, adj_mat, 'm', v, src_idx)
                    is_correct_mat = self.verify_correctness(pq_result[0], arr_mat_result[0])
                    print(f"{graph_name:<15} | {v:<10} | {'Array (Adj Matrix)':<25} | {arr_mat_time:<10.4f} | {arr_mat_mem:<12.4f} | {is_correct_mat}")
                    writer.writerow([density, v, 'Array(AdjMatrix)', round(arr_mat_time, 4), round(arr_mat_mem, 4)])
                    
                    print("-" * 90)
                    
        print("\nBenchmarking complete! Results saved to 'benchmark_results.csv'.")

if __name__ == "__main__":
    benchmarker = GraphBenchmarker()
    benchmarker.run_benchmarks()