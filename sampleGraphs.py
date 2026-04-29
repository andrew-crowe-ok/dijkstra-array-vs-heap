# All sample graphs as they appear in Section 5 of Project 2.
# Still need to generate our own DENSE_GRAPH_THREE.

# def add_adj_edge(list, start_node, end_node, weight):
#     list[start_node].append(end_node, weight)

# create adjacency list
def add_adj_edge(nodes, elements):
    # set number to nodes
    node_index = {}
    for i, node in enumerate(nodes):
        node_index[node] = i

    # intialize blank adj list
    adj_list = []
    for _ in range(len(nodes)):
        adj_list.append([])

    # put elements into adj list
    for start_node, end_node, weight in elements:
        adj_list[node_index[start_node]].append((end_node, weight))
        adj_list[node_index[end_node  ]].append((end_node, weight)) # for undirected graphs
    
    return adj_list    

def add_mat_edge(mat, n, m, weight):
    mat[n][m] = weight
    mat[m][n] = weight

SPARSE_GRAPH_ONE = {'A','B','C','D','E','F'}
SPARSE_EDGES_WEIGHTED_ONE= [
    ('A','B',4), ('A','C',2), ('B','D',5),
    ('C','D',1), ('D','E',3), ('E','F',2)
]
ADJ_LIST_SPARSE_GRAPH_ONE = add_adj_edge(SPARSE_GRAPH_ONE, SPARSE_EDGES_WEIGHTED_ONE)
print("Adj List Sparse Graph One: ", ADJ_LIST_SPARSE_GRAPH_ONE)

SPARSE_GRAPH_TWO = {1, 2, 3, 4, 5, 6, 7}
SPARSE_EDGES_WEIGHTED_TWO= [
    (1,2,3), (1,3,6), (2,4,2), (3,5,4),
    (4,6,7), (5,7,1), (2,5,5)
]
ADJ_LIST_SPARSE_GRAPH_TWO = add_adj_edge(SPARSE_GRAPH_TWO, SPARSE_EDGES_WEIGHTED_TWO)
print("Adj List Sparse Graph Two: ", ADJ_LIST_SPARSE_GRAPH_TWO)

DENSE_GRAPH_ONE = {'A','B','C','D','E'}
DENSE_EDGES_WEIGHTED_ONE= [
    ('A','B',2), ('A','C',5), ('A','D',1), ('A','E',4),
    ('B','C',3), ('B','D',2), ('B','E',6), ('C','D',3),
    ('C','E',1), ('D','E',2)
]
ADJ_LIST_DENSE_GRAPH_ONE = add_adj_edge(DENSE_GRAPH_ONE, DENSE_EDGES_WEIGHTED_ONE)
print("Adj List Dense Graph One: ", ADJ_LIST_DENSE_GRAPH_ONE)

DENSE_GRAPH_TWO = {1, 2, 3, 4, 5, 6}
DENSE_EDGES_WEIGHTED_TWO= [
    (1,2,3), (1,3,2), (1,4,6), (1,5,5), (1,6,4),
    (2,3,1), (2,4,2), (2,5,4), (2,6,7), (3,4,3),
    (3,5,6), (3,6,5), (4,5,2), (4,6,4), (5,6,1)
]
ADJ_LIST_DENSE_GRAPH_TWO = add_adj_edge(DENSE_GRAPH_TWO, DENSE_EDGES_WEIGHTED_TWO)
print("Adj List Dense Graph Two: ", ADJ_LIST_DENSE_GRAPH_TWO)

DENSE_GRAPH_THREE = {}
DENSE_EDGES_THREE= [

]