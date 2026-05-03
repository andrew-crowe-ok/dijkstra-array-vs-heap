import sys
import argparse
from priority_queue import DijkstraMinHeap
from dijkstra import pq_dijkstra, arr_dijkstra
from graph_utils import add_adj_list_edge, print_adj_list
from graph_utils import add_adj_mat_edge, print_adj_mat
from graph_data import (
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
        if(dijkstra_type == 'p'):
            print(f"\n{'='*40}")
            print(f"RUNNING PQ DIJKSTRA: {name}")
            print(f"{'='*40}")
        elif(dijkstra_type == 'a'):
            print(f"\n{'='*40}")
            print(f"RUNNING ARR DIJKSTRA: {name}")
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
            print("RUNNING PQ")
            distances, parents = pq_dijkstra(adj_list, len(nodes), src_idx)
        # FIX: added a nested if/elif here, the arr_dijkstra_mat command no longer crashes
        elif(dijkstra_type == 'a'):
            if(adj_type == 'l'):
              print("RUNNING ARR")
              distances, parents = arr_dijkstra(adj_list, adj_type, len(nodes), src_idx)
            elif(adj_type == 'm'):
              distances, parents = arr_dijkstra(adj_mat, adj_type, len(nodes), src_idx)
        
        # Output the shortest path results
        print(f"Shortest Paths from Source '{src_node}':")
        for i in range(len(nodes)):
            target_node = reverse_index[i]
            dist = distances[i]
            
            # Handle unreachable nodes
            if dist == sys.maxsize:
                print(f"Path to {target_node}: Unreachable")
            else:
                # Reconstruct the path using the parent array
                path = []
                curr = i
                while curr != -1:
                    path.append(reverse_index[curr])
                    curr = parents[curr]
                path.reverse()
                
                # Format and print the final path string
                path_str = " -> ".join(str(n) for n in path)
                print(f"Path to {target_node}: {path_str} (Distance: {dist})")

def run_performance_experiments():
    # Placeholder for 4.4 Step 4: Record Experimental Results
    print("Performance & Memory Experiments - Not yet implemented.")

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
    # Setup argument parser to select execution mode
    parser = argparse.ArgumentParser(description="CS361 Project 2: Dijkstra Implementations")
    parser.add_argument(
        'mode', 
        choices=['test_pq', 'pq_dijkstra', 'arr_dijkstra_list', 'arr_dijkstra_mat', 'benchmark'],
        help="Select the execution mode."
    )
    
    # Parse command line arguments
    args = parser.parse_args()

    # Execute the chosen mode
    if args.mode == 'test_pq':
        test_priority_queue()
    elif args.mode == 'pq_dijkstra':
        run_dijkstra('p', 'l')
    elif args.mode == 'arr_dijkstra_list':
        run_dijkstra('a', 'l') 
    elif args.mode == 'arr_dijkstra_mat':
        run_dijkstra('a', 'm') # TODO: currently broken
    elif args.mode == 'benchmark':
        run_performance_experiments()

if __name__ == "__main__":
    main()