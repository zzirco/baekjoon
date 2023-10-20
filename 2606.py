n = int(input())
pair = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(graph, v, visited):
    visited[v] = True
    global count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (n + 1)

dfs(graph, 1, visited)

print(count - 1)