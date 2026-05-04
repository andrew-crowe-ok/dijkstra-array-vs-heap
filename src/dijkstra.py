import sys
from src.priority_queue import DijkstraMinHeap

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
    dist[src_vertex] = 0                # Initialize start node (always 0)

    for _ in range(num_vertices):
        u = -1
        for v in range(num_vertices):
            # Find smallest unvisited node
            if not visited[v] and (u == -1 or dist[v] < dist[u]):
                u = v
        
        # Early exit if all remaining vertices are unreachable
        if dist[u] == sys.maxsize : break

        # This node has now been visited
        visited[u] = True

        # Run adj list
        if adj_type == 'l':
            arr_list(adj, u, dist, parent)
        # Run adj matrix
        elif adj_type == 'm':
            arr_mat(adj, u, dist, num_vertices, parent)
        else:
            # Error in case call is made incorrectly for debug, should never be seen by user
            sys.exit("ERROR! Function arr_dijkstra was called improperly!!\n"
                      "Should be called with 'l' for list or 'm' for matrix respectively!")

    # Returns distance and path taken
    return dist, parent

def arr_list(adj_list, u, dist, parent):
    for v, weight in adj_list[u]:
        # Relax Edge, check shortest known path
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight # New Shortest known distance found
            parent[v] = u              # Record path

def arr_mat(adj_matrix, u, dist, num_vertices, parent):
    for v in range(num_vertices):
        weight = adj_matrix[u][v]
        # If 0 no edge, skip
        # Assumes postive edges as Dijkstra does NOT support negatives
        if weight > 0:
            # Relax Edge
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight # New Shortest known distance found
                parent[v] = u              # Record path