"""Ex 3a - Blocks World planner (respects stacking constraints, BFS over states)"""
from collections import deque

initial = {"A": "B", "B": "table", "C": "table"}   # block -> what it sits on
goal    = {"A": "B", "B": "C",     "C": "table"}

def is_clear(state, block):
    return all(support != block for support in state.values())

def successors(state):
    for block in state:
        if not is_clear(state, block):
            continue
        for dest in list(state) + ["table"]:
            if dest == block or dest == state[block]:
                continue
            if dest != "table" and not is_clear(state, dest):
                continue
            new = dict(state)
            new[block] = dest
            yield (block, state[block], dest), new

def plan(start, target):
    key = lambda s: tuple(sorted(s.items()))
    queue, seen = deque([(start, [])]), {key(start)}
    while queue:
        state, moves = queue.popleft()
        if state == target:
            return moves
        for move, new in successors(state):
            if key(new) not in seen:
                seen.add(key(new))
                queue.append((new, moves + [move]))
    return None

print("Initial State:", initial)
print()
for block, src, dest in plan(initial, goal):
    print(f"Moving {block} from {src} to {dest}")
print("\nFinal Goal State Reached:", goal)

"""
OUTPUT:
Initial State: {'A': 'B', 'B': 'table', 'C': 'table'}

Moving A from B to table
Moving B from table to C
Moving A from table to B

Final Goal State Reached: {'A': 'B', 'B': 'C', 'C': 'table'}
"""
