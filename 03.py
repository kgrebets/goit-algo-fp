import heapq
import matplotlib.pyplot as plt
import networkx as nx

def find_dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph} 
    distances[start] = 0 
    heap = [(0, start)] 
    heapq.heapify(heap) 

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances

def visualize_graph(graph, shortest_paths, start):
    G = nx.Graph()
    for vertex, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(vertex, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold', edge_color='gray')
   
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)
    
    nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='lightgreen', node_size=2000)
    
    for vertex, distance in shortest_paths.items():
        if distance != float('inf') and vertex != start:
            nx.draw_networkx_nodes(G, pos, nodelist=[vertex], node_color='orange', node_size=2000)

    plt.title(f"Граф з найкоротшими шляхами від {start}")
    plt.show()

graph = {
    'A': [('B', 7), ('C', 9), ('F', 14)],
    'B': [('A', 7), ('C', 10), ('D', 15)],
    'C': [('A', 9), ('B', 10), ('D', 11), ('F', 2)],
    'D': [('B', 15), ('C', 11), ('E', 6)],
    'E': [('D', 6), ('F', 9)],
    'F': [('A', 14), ('C', 2), ('E', 9)]
}

start = 'A'  
shortest_paths = find_dijkstra(graph, start)
print(f"Найкоротші шляхи від вершини {start}: {shortest_paths}")

visualize_graph(graph, shortest_paths, start)
