import time
import tracemalloc
import csv
import random

from src.priority_queue import DijkstraMinHeap
from src.dijkstra import pq_dijkstra, arr_dijkstra
from src.graph_utils import add_adj_list_edge, print_adj_list
from src.graph_utils import add_adj_mat_edge, print_adj_mat

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
        
        # Hybrid graph generation algorithm
        if e_target > max_edges * 0.5: 
            # For dense graphs, pick edges to EXCLUDE to avoid the coupon collector problem
            num_to_exclude = max_edges - e_target
            excluded_edges = set()
            nodes_list = list(nodes)
            
            # Randomly select the minority of edges to leave out
            while len(excluded_edges) < num_to_exclude:
                u, dest = random.sample(nodes_list, 2)
                if u > dest: u, dest = dest, u 
                excluded_edges.add((u, dest))
            
            # Build the graph by iterating all possible pairs and skipping the excluded ones
            for i in range(v):
                for j in range(i+1, v):
                    u, dest = str(i), str(j)
                    if u > dest: u, dest = dest, u
                    
                    if (u, dest) not in excluded_edges:
                        edges.append((u, dest, random.randint(1, 100)))
        else:
            # For sparse/medium graphs, just pick edges to INCLUDE
            existing_edges = set()
            nodes_list = list(nodes)
            while len(edges) < e_target:
                u, dest = random.sample(nodes_list, 2)
                if u > dest: u, dest = dest, u 
                
                if (u, dest) not in existing_edges:
                    existing_edges.add((u, dest))
                    edges.append((u, dest, random.randint(1, 100)))
                    
        return nodes, edges

    def measure_execution(self, func, *args):
        """Measures runtime and peak memory usage in separate passes to minimize overhead."""
        runtimes = []
        peak_memories = []

        # Pass 1: Measure Time (No memory tracking overhead)
        for _ in range(self.trials):
            start_time = time.perf_counter()
            result = func(*args) # Save result from the last run for correctness check
            end_time = time.perf_counter()
            runtimes.append((end_time - start_time) * 1000) # Convert to ms

        # Pass 2: Measure Memory (Timing is ignored here)
        for _ in range(self.trials):
            tracemalloc.start()
            func(*args)
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            peak_memories.append(peak / (1024 * 1024)) # Convert to MB
        
        return result, runtimes, peak_memories

    # This function verifies correctness by assuming that the min-heap implementation of Dijkstra
    # is correct, then comparing the array versions against it. If there are no differences, it is
    # considered correct.
    def verify_correctness(self, dist_a, dist_b):
        """Verifies both implementations produced the same shortest path distances."""
        return dist_a == dist_b

    def run_benchmarks(self):
        """Main execution loop for all required experiments."""
        # Define uniform format strings to guarantee exact console alignment and prevent long lines
        header_fmt = "{:<15} | {:<25} | {:<6} | {:<10} | {:<12} | {}"
        row_fmt    = "{:<15} | {:<25} | {:<6} | {:<10.4f} | {:<12.4f} | {}"

        print(header_fmt.format('Graph Type', 'Method', 'Trial', 'Time (ms)', 'Memory (MB)', 'Correct'))
        print("-" * 87)

        densities = ['Sparse', 'Medium', 'Dense']

        # Open the CSV file for writing
        with open('benchmark_results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Density', 'Vertices', 'Method', 'Time_ms', 'Memory_MB'])

            for v in self.vertices_sizes:
                for density in densities:
                    # Generate Graph Data
                    nodes, edges = self.generate_test_data(v, density)
                    graph_name = f"{density}-{v}"
                    
                    # Build Adjacency Structures
                    adj_list, node_index = add_adj_list_edge(nodes, edges)
                    adj_mat, _ = add_adj_mat_edge(nodes, edges)
                    
                    src_node = sorted(list(nodes))[0]
                    src_idx = node_index[src_node]
                    
                    # Benchmark Priority Queue (Adjacency List) ---
                    pq_result, pq_times, pq_mems = self.measure_execution(pq_dijkstra, adj_list, v, src_idx)
                    
                    for i in range(self.trials):
                        print(row_fmt.format(graph_name, 'Min-Heap', i+1, pq_times[i], pq_mems[i], 'N/A'))
                    
                    pq_avg_time = sum(pq_times) / self.trials
                    pq_avg_mem = sum(pq_mems) / self.trials
                    print(row_fmt.format(graph_name, 'Min-Heap', 'AVG', pq_avg_time, pq_avg_mem, 'N/A'))
                    writer.writerow([density, v, 'minheap', round(pq_avg_time, 4), round(pq_avg_mem, 4)])
                    print("-" * 87)

                    # Benchmark Array (Adjacency List) ---
                    arr_list_result, arr_list_times, arr_list_mems = self.measure_execution(arr_dijkstra, adj_list, 'l', v, src_idx)
                    is_correct_list = self.verify_correctness(pq_result[0], arr_list_result[0])
                    
                    for i in range(self.trials):
                        print(row_fmt.format(graph_name, 'Array (Adj List)', i+1, arr_list_times[i], arr_list_mems[i], is_correct_list))
                    
                    arr_list_avg_time = sum(arr_list_times) / self.trials
                    arr_list_avg_mem = sum(arr_list_mems) / self.trials
                    print(row_fmt.format(graph_name, 'Array (Adj List)', 'AVG', arr_list_avg_time, arr_list_avg_mem, is_correct_list))
                    writer.writerow([density, v, 'arrlist', round(arr_list_avg_time, 4), round(arr_list_avg_mem, 4)])
                    print("-" * 87)

                    # Benchmark Array (Adjacency Matrix) ---
                    arr_mat_result, arr_mat_times, arr_mat_mems = self.measure_execution(arr_dijkstra, adj_mat, 'm', v, src_idx)
                    is_correct_mat = self.verify_correctness(pq_result[0], arr_mat_result[0])
                    
                    for i in range(self.trials):
                        print(row_fmt.format(graph_name, 'Array (Adj Matrix)', i+1, arr_mat_times[i], arr_mat_mems[i], is_correct_mat))
                    
                    arr_mat_avg_time = sum(arr_mat_times) / self.trials
                    arr_mat_avg_mem = sum(arr_mat_mems) / self.trials
                    print(row_fmt.format(graph_name, 'Array (Adj Matrix)', 'AVG', arr_mat_avg_time, arr_mat_avg_mem, is_correct_mat))
                    writer.writerow([density, v, 'arrmat', round(arr_mat_avg_time, 4), round(arr_mat_avg_mem, 4)])
                    print("=" * 87)
                    
        print("\nBenchmarking complete! Averages saved to 'benchmark_results.csv'.")

if __name__ == "__main__":
    benchmarker = GraphBenchmarker()
    benchmarker.run_benchmarks()