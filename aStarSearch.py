from queue import PriorityQueue

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
                f_score = tentative_g_score + heuristic[neighbor]
                open_list.put((f_score, neighbor))
                came_from[neighbor] = current
    
    return None  # No path found

# Example Graph with heuristic values
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'G': 12},
    'B': {'C': 2},
    'C': {'G': 3},
    'G': {}
}

heuristic = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'G': 0}  # Estimated cost to goal

path = a_star_search(graph, 'S', 'G', heuristic)
print("A* Path:", path)
