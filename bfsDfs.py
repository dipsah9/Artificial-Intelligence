# Graph implementation using adjacency list
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(self.graph.get(node, []))

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        if start not in visited:
            print(start, end=' ')
            visited.add(start)
            for neighbor in self.graph.get(start, []):
                self.dfs(neighbor, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("BFS Traversal:")
g.bfs(0)

print("\nDFS Traversal:")
g.dfs(0)
