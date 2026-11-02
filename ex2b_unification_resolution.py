"""Ex 2b - Unification and Resolution
Terms are lists, e.g. ["Human", "John"]. Lowercase strings are variables."""

def is_var(x):
    return isinstance(x, str) and x[:1].islower()

def unify(x, y, theta):
    if theta is None:
        return None
    if x == y:
        return theta
    if is_var(x):
        return unify_var(x, y, theta)
    if is_var(y):
        return unify_var(y, x, theta)
    if isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    if isinstance(x, str) and x in theta:
        return unify(var, theta[x], theta)
    new = dict(theta)
    new[var] = x
    return new

def substitute(term, theta):
    if isinstance(term, list):
        return [substitute(t, theta) for t in term]
    return substitute(theta[term], theta) if term in theta else term

# Knowledge base
facts = [["Human", "John"]]
rules = [  # (premises, conclusion):  Human(x) -> Mortal(x)
    ([["Human", "x"]], ["Mortal", "x"]),
]

def resolve(goal):
    """Backward resolution: prove goal from facts or by resolving with a rule."""
    for f in facts:
        if unify(goal, f, {}) is not None:
            return True
    for premises, conclusion in rules:
        theta = unify(conclusion, goal, {})
        if theta is not None and all(resolve(substitute(p, theta)) for p in premises):
            return True
    return False

print("Unify Human(x) with Human(John):", unify(["Human", "x"], ["Human", "John"], {}))
query = ["Mortal", "John"]
if resolve(query):
    print("Query is resolved: John is Mortal")
else:
    print("Query could not be resolved")

"""
OUTPUT:
Unify Human(x) with Human(John): {'x': 'John'}
Query is resolved: John is Mortal
"""
