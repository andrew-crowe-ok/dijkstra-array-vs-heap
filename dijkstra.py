import sys
from priority_queue import DijkstraMinHeap

def dijkstra_array_matrix(adj_mat, num_vertices, src_vertex):
    pass

def dijkstra_array_list(adj_list, num_vertices, src_vertex):
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