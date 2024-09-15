# DFS example

def dfs(graph, root):
    visited = set()
    def dfs_helper(node):
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)
    dfs_helper(root)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'F'],
    'D': ['B'],
    'F': ['C']
}
dfs(graph, 'A')  # A B D C F