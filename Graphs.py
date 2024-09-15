# Graph example
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'F'],
    'D': ['B'],
    'F': ['C']
}
print(graph['A'])  # ['B', 'C']