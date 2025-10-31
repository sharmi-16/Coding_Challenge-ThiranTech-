from collections import deque
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'J', 'I'],  
    'J': ['C', 'K'],
    'K': ['J', 'L'],
    'L': ['K', 'D'],
    'D': ['L', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G'],
    'G': ['F', 'M', 'H'],
    'H': ['G', 'N'],
    'N': ['H', 'M'],
    'M': ['N', 'G'],
    'I': ['C']              
}
def find_junctions(graph):
    junctions = [station for station, connections in graph.items() if len(connections) > 2]
    return junctions
def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        station, path = queue.popleft()
        if station == goal:
            return path

        for neighbor in graph[station]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))


junctions = find_junctions(graph)
print("Junction Stations:",junctions)

path = bfs_path(graph, 'A', 'E')
print("Path from Krish (A) to Varun (E):", ' -> '.join(path))
print("Number of junctions Krish should travel:", len(path) - 1)
