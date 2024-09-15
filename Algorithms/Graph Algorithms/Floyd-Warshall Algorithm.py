# Floyd-Warshall Algorithm example

def floyd_warshall(graph):
    distances = {node: {neighbor: float('infinity') for neighbor in graph} for node in graph}
    for node in graph:
        distances[node][node] = 0
        for neighbor, weight in graph[node].items():
            distances[node][neighbor] = weight
    for intermediate in graph:
        for start in graph:
            for end in graph:
                distance = distances[start][intermediate] + distances[intermediate][end]
                if distance < distances[start][end]:
                    distances[start][end] = distance
    return distances

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 3, 'F': 1},
    'D': {'B': 2, 'E': 1},
    'F': {'C': 1, 'E': 1}
}
print(floyd_warshall(graph))