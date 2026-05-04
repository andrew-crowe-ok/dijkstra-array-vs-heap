# create adjacency list
def add_adj_list_edge(nodes, elements):
    
    # Set number to nodes
    # Sorted(list()) is retained to ensure sets map to deterministic indices.
    node_index = {}
    for i, node in enumerate(sorted(list(nodes))):
        node_index[node] = i

    # Intialize blank adj list
    vert = len(nodes)
    adj_list = [[] for _ in range(vert)]

    # Put elements into adj list
    for start_node, end_node, weight in elements:
        u, v = node_index[start_node], node_index[end_node]
        adj_list[u].append((v, weight))
        
        # Append the reverse connection (u, weight) for undirected graphs.
        adj_list[v].append((u, weight)) # for undirected graphs
    
    # Must return node_index alongside adj_list for priority queue initialization
    return adj_list, node_index    

# Print formated list
def print_adj_list(adj_list):
    for i in range(len(adj_list)):
        print(f"{i}: ", end="")
        for j in adj_list[i]:
            print(f"{{{j[0]}, {j[1]}}} ", end="")
        print()
    print()

# Create adj matrix
def add_adj_mat_edge(nodes, elements):
    # Set number to nodes
    node_index = {}
    for i, node in enumerate(sorted(list(nodes))):
        node_index[node] = i

    # Intialize blank adj list
    vert = len(nodes)
    adj_mat = [[0] * vert for _ in range(vert)]

    # Put elements into adj list
    for start_node, end_node, weight in elements:
        row, col = node_index[start_node], node_index[end_node]
        adj_mat[row][col] = weight
        adj_mat[col][row] = weight # For undirected graphs

    return adj_mat, node_index

# Print matrix
def print_adj_mat(adj_mat):
    for row in adj_mat:
        print(row)
    print()