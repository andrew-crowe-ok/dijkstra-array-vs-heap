from priority_queue import DijkstraMinHeap
from graph_utils import add_adj_list_edge, print_adj_list
from graph_data import (
    SPARSE_NODES_ONE, SPARSE_EDGES_ONE,
    SPARSE_NODES_TWO, SPARSE_EDGES_TWO,
    DENSE_NODES_ONE, DENSE_EDGES_ONE,
    DENSE_NODES_TWO, DENSE_EDGES_TWO,
    get_dense_graph_three
)

def main():
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
            
        # Force the the lowest priority element in the 
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

if __name__ == "__main__":
    main()