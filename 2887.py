def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(edges, v):
    parent = [0] * (v + 1)
    for i in range(1, v + 1):
        parent[i] = i
    edges.sort()
    mst = []
    for e in edges:
        cost, a, b, = e
        if find_parent(parent, a) != find_parent(parent, b):
            mst.append((cost, a, b))
            union_parent(parent, a, b)
    return mst

v = int(input())

planets = []
for i in range(v):
    x, y, z = list(map(int, input().split()))
    planets.append((i, x, y, z))

edges = []
for i in [1,2,3]:
    sort = sorted(planets, key = lambda x: x[i])
    e = [(abs(b[i] - a[i]), a[0], b[0]) for a, b in zip(sort[:-1], sort[1:])]
    edges += e

mst = kruskal(edges, v)
total_cost = sum([e[0] for e in mst])
print(total_cost)