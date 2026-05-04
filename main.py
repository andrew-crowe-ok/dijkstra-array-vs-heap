import sys
import argparse
from src.priority_queue import DijkstraMinHeap
from src.dijkstra import pq_dijkstra, arr_dijkstra
from src.graph_utils import add_adj_list_edge, print_adj_list
from src.graph_utils import add_adj_mat_edge, print_adj_mat
from src.graph_data import (
    SPARSE_NODES_ONE, SPARSE_EDGES_ONE,
    SPARSE_NODES_TWO, SPARSE_EDGES_TWO,
    DENSE_NODES_ONE, DENSE_EDGES_ONE,
    DENSE_NODES_TWO, DENSE_EDGES_TWO,
    get_dense_graph_three
)

def run_dijkstra(dijkstra_type, adj_type):
    test_graphs = get_test_graphs()

    for name, nodes, edges in test_graphs:
        # Both dijkstra can use this code, only difference is printing & funct calls
        if dijkstra_type == 'p':
            print(f"\n{'='*40}")
            print(f"{'RUNNING MINHEAP DIJKSTRA':^40}")
            print(f"{name:^40}")
            print(f"{'='*40}")
        elif dijkstra_type == 'a':
            if adj_type == 'l':
                print(f"\n{'='*40}")
                print(f"{'RUNNING ARR (ADJ LIST) DIJKSTRA':^40}")
                print(f"{name:^40}")
                print(f"{'='*40}")
            elif adj_type == 'm':
                print(f"\n{'='*40}")
                print(f"{'RUNNING ARR (ADJ MATRIX) DIJKSTRA':^40}")
                print(f"{name:^40}")
                print(f"{'='*40}")
        else:
            # Error in case call is made incorrectly for debug, should never be seen by user
            sys.exit("ERROR! Function run_dijkstra was called improperly!!\n"
                      "Should be called with 'a' for array or 'p' for prority queue respectively!")
        
        # Build the adjacency list, map the set of vertices to an indexed list of nodes
        adj_list, node_index = add_adj_list_edge(nodes, edges)
        # currently just for testing
        adj_mat, node_index = add_adj_mat_edge(nodes, edges)
        
        # Create a reverse index to map node indices back to original node names
        reverse_index = {v: k for k, v in node_index.items()}
        
        # Select the first node in the sorted set as the source vertex
        src_node = sorted(list(nodes))[0]
        src_idx = node_index[src_node]
        
        # Execute Dijkstra's algorithm to get shortest paths and parent array
        if(dijkstra_type == 'p'):
            distances, parents = pq_dijkstra(adj_list, len(nodes), src_idx)
        elif(dijkstra_type == 'a'):
            # Nested if/elif here, ensuring that the
            # correct adjacency structure is passed to arr_dijkstra()
            if(adj_type == 'l'):
              distances, parents = arr_dijkstra(adj_list, adj_type, len(nodes), src_idx)
            elif(adj_type == 'm'):
              distances, parents = arr_dijkstra(adj_mat, adj_type, len(nodes), src_idx)
        
      # Output the shortest path results
        print(f"Shortest Paths from Source '{src_node}':")
        
        path_outputs = []
        max_path_len = 0

        # Pass 1: Construct path strings and find the maximum length
        for i in range(len(nodes)):
            target_node = reverse_index[i]
            dist = distances[i]
            
            # Handle unreachable nodes
            if dist == sys.maxsize:
                path_prefix = f"Path to {target_node}: Unreachable"
                distance_suffix = ""
            else:
                # Reconstruct the path using the parent array
                path = []
                curr = i
                while curr != -1:
                    path.append(reverse_index[curr])
                    curr = parents[curr]
                path.reverse()
                
                # Format the path prefix
                path_str = " -> ".join(str(n) for n in path)
                path_prefix = f"Path to {target_node}: {path_str}"
                distance_suffix = f"  Distance: {dist}"
            
            # Store the components and track the longest path string
            path_outputs.append((path_prefix, distance_suffix))
            if len(path_prefix) > max_path_len:
                max_path_len = len(path_prefix)
        
        # Pass 2: Format and combine into a single string
        final_output_lines = []
        for prefix, suffix in path_outputs:
            if suffix:
                # Left-align the prefix to max_path_len to push the suffix to the right
                final_output_lines.append(f"{prefix:<{max_path_len}} {suffix}")
            else:
                final_output_lines.append(prefix)
                
        # Output all results at once
        print("\n".join(final_output_lines))

def run_performance_experiments():
    from src.benchmarker import GraphBenchmarker
    bench = GraphBenchmarker()
    bench.run_benchmarks()

def get_test_graphs():
    # Generate a third dense graph
    dyn_nodes, dyn_edges = get_dense_graph_three()

    # Groups all the graphs into a list for processing
    test_graphs = [
        ("Sparse Graph One", SPARSE_NODES_ONE, SPARSE_EDGES_ONE),
        ("Sparse Graph Two", SPARSE_NODES_TWO, SPARSE_EDGES_TWO),
        ("Dense Graph One", DENSE_NODES_ONE, DENSE_EDGES_ONE),
        ("Dense Graph Two", DENSE_NODES_TWO, DENSE_EDGES_TWO),
        ("Dynamic Dense Graph", dyn_nodes, dyn_edges)
    ]
    return test_graphs

def test_priority_queue():
    # Retrieve the grouped list of test graphs
    test_graphs = get_test_graphs()

    # Loop through each graph and print debug output
    for name, nodes, edges in test_graphs:
        print(f"\n{'='*40}")
        print(f"TESTING: {name}")
        print(f"{'='*40}")

        # Build the adjacency list, map the set of vertices to an indexed list of nodes
        # Ex: the set of vertices {'A'...'F'} is mapped to node_index[0]...node_index[5]
        adj_list, node_index = add_adj_list_edge(nodes, edges)
        
        print("\n[1] Adjacency List Structure:")
        print_adj_list(adj_list)

        # Initialize a priority queue of capacity equal to the graph size
        vert_count = len(nodes)
        pq = DijkstraMinHeap(max_vertices=vert_count, debug=False)
        
        # Populate the pq with all vertices in the graph 
        # and assign them predictable test distances.
        for node in nodes:
            v_idx = node_index[node]
            mock_dist = vert_count - v_idx
            pq.insertKey(v_idx, mock_dist)
            
        # Force the lowest priority element in the 
        # pq to the front of the pq/top of the heap
        if not pq.is_empty():
            pq.decreaseKey(0, -1)

        # Output that verifies the correctness of 
        # insertKey, minHeapify, and decreaseKey
        # operations for each graph. 
        print("\n[2] Min Heap Extraction Order (Expected: Distances in ascending order):")
        while not pq.is_empty():
            item = pq.extractMin()
            print(f"Vertex Index: {item[1]} | Distance: {item[0]}")

def main():
    parser = argparse.ArgumentParser(
        description="CS361 Project 2: Dijkstra Implementations",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    subparsers = parser.add_subparsers(
        dest="mode", 
        required=True, 
        title="Execution Modes", 
        metavar="COMMAND"
    )

    # test_pq
    parser_test = subparsers.add_parser(
        'test', 
        aliases=['pqt', 'pq_test'], 
        help="Run Priority Queue insertion and extraction tests"
    )
    parser_test.set_defaults(func=lambda _: test_priority_queue())

    # pq_dijkstra
    parser_pq = subparsers.add_parser(
        'minheap', 
        aliases=['pq', 'pq_dijkstra'], 
        help="Execute Dijkstra's algorithm using a Min-Heap Priority Queue (Adjacency List)"
    )
    parser_pq.set_defaults(func=lambda _: run_dijkstra('p', 'l'))

    # arr_dijkstra_list
    parser_arr_l = subparsers.add_parser(
        'arrlist', 
        aliases=['al', 'arr_dijkstra_list'], 
        help="Execute Dijkstra's using an Array-based Priority Queue (Adjacency List)"
    )
    parser_arr_l.set_defaults(func=lambda _: run_dijkstra('a', 'l'))

    # arr_dijkstra_mat
    parser_arr_m = subparsers.add_parser(
        'arrmat', 
        aliases=['am', 'arr_dijkstra_mat'], 
        help="Execute Dijkstra's using an Array-based Priority Queue (Adjacency Matrix)"
    )
    parser_arr_m.set_defaults(func=lambda _: run_dijkstra('a', 'm'))

    # benchmark
    parser_bench = subparsers.add_parser(
        'bench', 
        aliases=['b', 'benchmark'], 
        help="Run GraphBenchmarker performance experiments"
    )
    parser_bench.set_defaults(func=lambda _: run_performance_experiments())

    def custom_error(message):
          if "invalid choice" in message:
              print(f"\nERROR: Unrecognized command.")
              print(f"Please use one of the valid execution modes.")
              print(f"Run 'python main.py --help' to see all available commands.\n")
          else:
              print(f"\nERROR: {message}\n")
          sys.exit(1)
          
    parser.error = custom_error

    # Parse and execute
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
