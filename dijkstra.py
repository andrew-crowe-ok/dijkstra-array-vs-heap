import sys
from priority_queue import DijkstraMinHeap

def array_matrix_dijkstra(adj_mat, num_vertices, src_vertex):
    pass

def array_list_dijkstra(adj_list, num_vertices, src_vertex):
    pass

def pq_dijkstra(adj_list, num_vertices, src_vertex):
    distances = [sys.maxsize] * num_vertices
    parents = [-1] * num_vertices # Initialize parents array
    distances[src_vertex] = 0
    
    pq = DijkstraMinHeap(max_vertices=num_vertices)
    
    for v in range(num_vertices):
        pq.insertKey(v, distances[v])
        
    while not pq.is_empty():
        min_node = pq.extractMin()
        current_dist = min_node[0]  # Unused but kept for clarity
        current_vertex = min_node[1]
        
        for neighbor, weight in adj_list[current_vertex]:
            if pq.isInMinHeap(neighbor) and distances[current_vertex] != sys.maxsize:
                new_dist = distances[current_vertex] + weight
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parents[neighbor] = current_vertex # EXTRA CREDIT -- Record the path
                    pq.decreaseKey(neighbor, new_dist)
                    
    return distances, parents # Return both arrays

def arr_dijkstra(adj, adj_type, num_vertices, src_vertex):
    dist = [sys.maxsize] * num_vertices # Initialize path weight
    visited = [False] * num_vertices    # Has the node been vistied
    parent = [-1] * num_vertices        # Initialize parents array
    dist[src_vertex] = 0

    for _ in range(num_vertices):
        u = -1
        for v in range(num_vertices):
            if not visited[v] and (u == -1 or dist[v] < dist[u]):
                u = v
        
        if dist[u] == sys.maxsize : break

        visited[u] = True

        if adj_type == 'l':
            #print("RUNNING ADJ LIST")
            arr_list(adj, u, dist, parent)
        elif adj_type == 'm':
            print("RUNNING ADJ MATRIX")
            arr_mat(adj, u, dist, num_vertices, parent)
        else:
            # Error in case call is made incorrectly for debug, should never be seen by user
            sys.exit("ERROR! Function arr_dijkstra was called improperly!!\n"
                      "Should be called with 'l' for list or 'm' for matrix respectively!")

    return dist, parent

def arr_list(adj_list, u, dist, parent):
    for v, weight in adj_list[u]:
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            parent[v] = u

def arr_mat(adj_matrix, u, dist, num_vertices, parent):
    # TODO: Currently breaks since nodes are not always integers
    for v, weight in num_vertices:
        weight = adj_matrix[u][v]
        if weight > 0:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u