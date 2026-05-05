import sys
import random
from src.priority_queue import DijkstraMinHeap

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

# Generate spanning tree, sparse graph
def get_spanning_tree_graph(seed=37):
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

    print(f"\n{'='*40}")
    print(f"GENERATING SPARSE SPANNING TREE GRAPH")
    print(f"{'='*40}")
    print(f"Nodes              : {rand_v}")

    return DENSE_GRAPH_THREE, DENSE_EDGES_THREE

# Generate graph via prim's algo
def build_spantree_prim(num_vertices, weight_range, pq):
    distances = [sys.maxsize] * num_vertices # Initialize path weight
    visited = [False] * num_vertices         # Has the node been vistied
    parent = [-1] * num_vertices             # Initialize parents array

    # Insert all with infinity
    for v in range(num_vertices):
        pq.insertKey(v, sys.maxsize)

    # Start from node 0, 0
    pq.decreaseKey(0, 0)

    edges_set = set()
    edge_list = []

    while not pq.is_empty():
        min_node = pq.extractMin()
        if min_node is None:
            break
        
        _, u =  min_node
        visited[u] = True

        # Record the edge that brought u into the tree
        if parent[u] != -1:
            p, weight = parent[u], distances[u]
            key = (min(p, u), max(p, u))
            if key not in edges_set:
                edges_set.add(key)
                edge_list.append((p, u, weight))
        
        for v in range(num_vertices):
            if not visited[v] and pq.isInMinHeap(v):
                weight = random.randint(*weight_range)
                current_key = pq.harr[pq.pos[v]][0]
                if weight < current_key:      # only update if this edge is cheaper
                    parent[v] = u
                    distances[v] = weight
                    pq.decreaseKey(v, weight) # sift-up to maintain heap property

    return edges_set, edge_list

# Create and return graph
def get_dense_graph_rand(num_vertices=18, density=0.7, weight_range=(1, 20), seed=37):
    # Randomly generated graph
    # build random (seeded for repeatable results)
    if seed is not None:
        random.seed(seed)
    
    # create all nodes
    DENSE_GRAPH_THREE = set(range(num_vertices))

    pq = DijkstraMinHeap(num_vertices)
    DENSE_EDGE_SET, DENSE_EDGES_THREE = build_spantree_prim(num_vertices, weight_range, pq)

    max_edges    = num_vertices * (num_vertices - 1) // 2 # We want a dense graph
    target       = int(max_edges * density)               # how dense the graph should be                       
    max_attempts = target * 10                            # Ensures no infinite loops

    attempts = 0
    while len(DENSE_EDGE_SET) < target and attempts < max_attempts:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)

        if u == v:
            attempts += 1
            continue

        key = (min(v, u), max(v, u))
        if key in DENSE_EDGE_SET:
            attempts += 1
            continue

        weight = random.randint(*weight_range)
        DENSE_EDGE_SET.add(key)
        DENSE_EDGES_THREE.append((u, v, weight))
        attempts = 0 # reset

    print(f"\n{'='*40}")
    print(f"GENERATING DENSE GRAPH")
    print(f"{'='*40}")
    actual_density = len(DENSE_EDGE_SET) / max_edges if max_edges > 0 else 0
    print(f"Nodes              : {num_vertices}")
    print(f"Max possible edges : {max_edges}")
    print(f"Target edges       : {target}  ({density*100:.0f}% density)")
    print(f"Actual edges       : {len(DENSE_EDGE_SET)}  ({actual_density*100:.1f}% density)")

    return DENSE_GRAPH_THREE, DENSE_EDGES_THREE