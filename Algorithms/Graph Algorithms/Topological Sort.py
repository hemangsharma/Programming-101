# Topological Sort example

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    queue = [node for node in graph if in_degree[node] == 0]
    sorted_nodes = []
    while queue:
        node = queue.pop(0)
        sorted_nodes.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_nodes

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'F'],
    'D': ['E'],
    'F': ['E']
}
print(topological_sort(graph))  # ['A', 'C', 'B', 'F', 'D', 'E']