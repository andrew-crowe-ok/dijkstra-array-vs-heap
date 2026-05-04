import random

# Sparse Graph One
SPARSE_NODES_ONE = {'A','B','C','D','E','F'}
SPARSE_EDGES_ONE = [
    ('A','B',4), ('A','C',2), ('B','D',5),
    ('C','D',1), ('D','E',3), ('E','F',2)
]

# Sparse Graph Two
SPARSE_NODES_TWO = {1, 2, 3, 4, 5, 6, 7}
SPARSE_EDGES_TWO = [
    (1,2,3), (1,3,6), (2,4,2), (3,5,4),
    (4,6,7), (5,7,1), (2,5,5)
]

# Dense Graph One
DENSE_NODES_ONE = {'A','B','C','D','E'}
DENSE_EDGES_ONE = [
    ('A','B',2), ('A','C',5), ('A','D',1), ('A','E',4),
    ('B','C',3), ('B','D',2), ('B','E',6), ('C','D',3),
    ('C','E',1), ('D','E',2)
]

# Dense Graph Two
DENSE_NODES_TWO = {1, 2, 3, 4, 5, 6}
DENSE_EDGES_TWO = [
    (1,2,3), (1,3,2), (1,4,6), (1,5,5), (1,6,4),
    (2,3,1), (2,4,2), (2,5,4), (2,6,7), (3,4,3),
    (3,5,6), (3,6,5), (4,5,2), (4,6,4), (5,6,1)
]

def get_dense_graph_three(seed=37):
    # Randomly generated graph
    # build random (seeded for repeatable results)
    random.seed(seed)
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
    DENSE_EDGES_THREE = []
    # connects all the edges
    for i in range(rand_v - 1):
        # create straight line of nodes
        # 0 - 1 - 2 - 3 ... rand_v
        # spanning tree, no cycles no nodes left unconnected 
        DENSE_EDGES_THREE.append((i, i + 1, random.randint(1, rand_v)))
        
    for i in range(rand_v):
        DENSE_EDGES_THREE.append((random.randint(0, rand_v - 1), # start node
                                  random.randint(0, rand_v - 1), # end node
                                  random.randint(1, rand_v)))    # weight
                                  
    return DENSE_GRAPH_THREE, DENSE_EDGES_THREE