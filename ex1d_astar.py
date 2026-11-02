"""Ex 1d - A* search on a warehouse grid"""
import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position, self.parent = position, parent
        self.g, self.h, self.f = g, h, g + h
    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [Node(start, None, 0, heuristic(start, goal))]
    closed_set = set()
    while open_list:
        cur = heapq.heappop(open_list)
        if cur.position == goal:
            path = []
            while cur:
                path.append(cur.position)
                cur = cur.parent
            return path[::-1]
        if cur.position in closed_set:
            continue
        closed_set.add(cur.position)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = cur.position[0] + dr, cur.position[1] + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and (r, c) not in closed_set:
                heapq.heappush(open_list, Node((r, c), cur, cur.g + 1, heuristic((r, c), goal)))
    return None

warehouse_grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
print("Optimal Path:", a_star(warehouse_grid, (0, 0), (4, 4)))

"""
OUTPUT:
Optimal Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
"""
