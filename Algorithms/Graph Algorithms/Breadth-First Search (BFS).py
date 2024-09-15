# BFS example
from collections import deque

def bfs(graph, root):
    visited = set()
    queue = deque([root])
    visited.add(root)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'F'],
    'D': ['B'],
    'F': ['C']
}
bfs(graph, 'A') 