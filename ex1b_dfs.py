"""Ex 1b - Depth First Search on a warehouse graph"""
warehouse_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path.append(start)
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path[:])
            if result:
                return result
    return None

start_node, goal_node = 'A', 'F'
print(f"DFS Path from {start_node} to {goal_node}: {dfs(warehouse_graph, start_node, goal_node)}")

"""
OUTPUT:
DFS Path from A to F: ['A', 'B', 'E', 'F']
"""
