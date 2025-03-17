from queue import PriorityQueue
import math

def a_star_search(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((0, start))  # (cost, node)
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    while not open_list.empty():
        _, current = open_list.get()
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                open_list.put((f_score, neighbor))
                came_from[neighbor] = current
    
    return None  # No path found

def manhattan_heuristic(node, goal):
    h_values = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'G': 0}  # Example heuristic values
    return h_values[node]

def euclidean_heuristic(node, goal):
    coordinates = {'S': (0, 0), 'A': (1, 2), 'B': (2, 3), 'C': (4, 4), 'G': (5, 5)}
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Example Graph with costs
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'G': 12},
    'B': {'C': 2},
    'C': {'G': 3},
    'G': {}
}

print("A* with Manhattan Distance Heuristic:")
path_manhattan = a_star_search(graph, 'S', 'G', manhattan_heuristic)
print("Path:", path_manhattan)

print("\nA* with Euclidean Distance Heuristic:")
path_euclidean = a_star_search(graph, 'S', 'G', euclidean_heuristic)
print("Path:", path_euclidean)
