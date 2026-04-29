import random # used to generate Dense Graph 3
# All sample graphs as they appear in Section 5 of Project 2.

# create adjacency list
def add_adj_list_edge(nodes, elements):
    # set number to nodes
    node_index = {}
    for i, node in enumerate(nodes):
        node_index[node] = i

    # intialize blank adj list
    vert = len(nodes)
    adj_list = [[] for _ in range(vert)]

    # put elements into adj list
    for start_node, end_node, weight in elements:
        adj_list[node_index[start_node]].append((end_node, weight))
        adj_list[node_index[end_node  ]].append((end_node, weight)) # for undirected graphs
    
    return adj_list    

# print formated list
def print_adj_list(adj_list):
    for i in range(len(adj_list)):
        print(f"{i}: ", end="")
        for j in adj_list[i]:
            print(f"{{{j[0]}, {j[1]}}} ", end="")
        print()
    print()

# create adj matrix
def add_adj_mat_edge(nodes, elements):
    # set number to nodes
    node_index = {}
    for i, node in enumerate(nodes):
        node_index[node] = i

    # intialize blank adj list
    vert = len(nodes)
    adj_mat = [[0] * vert for _ in range(vert)]

    # put elements into adj list
    for start_node, end_node, weight in elements:
        row, col = node_index[start_node], node_index[end_node]
        adj_mat[row][col] = weight
        adj_mat[col][row] = weight # for undirected graphs

    return adj_mat

# print matrix
def print_adj_mat(adj_mat):
    for row in adj_mat:
        print(row)
    print()

SPARSE_GRAPH_ONE = {'A','B','C','D','E','F'}
SPARSE_EDGES_WEIGHTED_ONE= [
    ('A','B',4), ('A','C',2), ('B','D',5),
    ('C','D',1), ('D','E',3), ('E','F',2)
]
ADJ_LIST_SPARSE_GRAPH_ONE = add_adj_list_edge(SPARSE_GRAPH_ONE, SPARSE_EDGES_WEIGHTED_ONE)
print("Adj List Sparse Graph One: ")
print_adj_list(ADJ_LIST_SPARSE_GRAPH_ONE)
ADJ_MAT_SPARSE_GRAPH_ONE = add_adj_mat_edge(SPARSE_GRAPH_ONE, SPARSE_EDGES_WEIGHTED_ONE)
print("Adj Matrix Sparse Graph One: ")
print_adj_mat(ADJ_MAT_SPARSE_GRAPH_ONE)

SPARSE_GRAPH_TWO = {1, 2, 3, 4, 5, 6, 7}
SPARSE_EDGES_WEIGHTED_TWO= [
    (1,2,3), (1,3,6), (2,4,2), (3,5,4),
    (4,6,7), (5,7,1), (2,5,5)
]
ADJ_LIST_SPARSE_GRAPH_TWO = add_adj_list_edge(SPARSE_GRAPH_TWO, SPARSE_EDGES_WEIGHTED_TWO)
print("Adj List Sparse Graph Two: ")
print_adj_list(ADJ_LIST_SPARSE_GRAPH_TWO)
ADJ_MAT_SPARSE_GRAPH_TWO = add_adj_mat_edge(SPARSE_GRAPH_TWO, SPARSE_EDGES_WEIGHTED_TWO)
print("Adj Matrix Sparse Graph One: ")
print_adj_mat(ADJ_MAT_SPARSE_GRAPH_TWO)

DENSE_GRAPH_ONE = {'A','B','C','D','E'}
DENSE_EDGES_WEIGHTED_ONE= [
    ('A','B',2), ('A','C',5), ('A','D',1), ('A','E',4),
    ('B','C',3), ('B','D',2), ('B','E',6), ('C','D',3),
    ('C','E',1), ('D','E',2)
]
ADJ_LIST_DENSE_GRAPH_ONE = add_adj_list_edge(DENSE_GRAPH_ONE, DENSE_EDGES_WEIGHTED_ONE)
print("Adj List Dense Graph One: ") 
print_adj_list(ADJ_LIST_DENSE_GRAPH_ONE)
ADJ_MAT_DENSE_GRAPH_ONE = add_adj_mat_edge(DENSE_GRAPH_ONE, DENSE_EDGES_WEIGHTED_ONE)
print("Adj Matrix Dense Graph One: ")
print_adj_mat(ADJ_MAT_DENSE_GRAPH_ONE)

DENSE_GRAPH_TWO = {1, 2, 3, 4, 5, 6}
DENSE_EDGES_WEIGHTED_TWO= [
    (1,2,3), (1,3,2), (1,4,6), (1,5,5), (1,6,4),
    (2,3,1), (2,4,2), (2,5,4), (2,6,7), (3,4,3),
    (3,5,6), (3,6,5), (4,5,2), (4,6,4), (5,6,1)
]
ADJ_LIST_DENSE_GRAPH_TWO = add_adj_list_edge(DENSE_GRAPH_TWO, DENSE_EDGES_WEIGHTED_TWO)
print("Adj List Dense Graph Two: ")
print_adj_list(ADJ_LIST_DENSE_GRAPH_TWO)
ADJ_MAT_DENSE_GRAPH_TWO = add_adj_mat_edge(DENSE_GRAPH_TWO, DENSE_EDGES_WEIGHTED_TWO)
print("Adj Matrix Dense Graph Two: ")
print_adj_mat(ADJ_MAT_DENSE_GRAPH_TWO)

# Randomly generated graph
# build random (seeded for repeatable results)
random.seed(37)
DENSE_GRAPH_THREE = set()

# generate random vertex
rand_v = random.randint(10, 20)
#print(rand_v)

# create nodes
i = 0
while i < rand_v:
    DENSE_GRAPH_THREE.add(i)
    i += 1
#print(DENSE_GRAPH_THREE)

# generate edges
DENSE_EDGES_THREE = [[] for _ in range(rand_v)]
# connects all the edges
for i in range(rand_v - 1):
    # create straight line of nodes
    # 0 - 1 - 2 - 3 ... rand_v
    # spanning tree, no cycles no nodes left unconnected 
    DENSE_EDGES_THREE.append((i, i + 1, random.randint(1, rand_v)))
    
for i in range(rand_v):
    DENSE_EDGES_THREE[i] = (random.randint(0, rand_v - 1), # start node
                            random.randint(0, rand_v - 1), # end node
                            random.randint(1, rand_v))     # weight
#print(DENSE_EDGES_THREE)
ADJ_LIST_DENSE_GRAPH_THREE = add_adj_list_edge(DENSE_GRAPH_THREE, DENSE_EDGES_THREE)
print("Adj List Dense Graph Three: ")
print_adj_list(ADJ_LIST_DENSE_GRAPH_THREE)
ADJ_MAT_DENSE_GRAPH_THREE = add_adj_mat_edge(DENSE_GRAPH_THREE, DENSE_EDGES_THREE)
print("Adj Matrix Dense Graph Three: ")
print_adj_mat(ADJ_MAT_DENSE_GRAPH_THREE)