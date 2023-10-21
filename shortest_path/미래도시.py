INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for q in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][q] + graph[q][j])

x, k = map(int, input().split())

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("F", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()

if graph[1][k] != INF and graph[k][x] != INF:
    print(graph[1][k] + graph[k][x])
else:
    print("-1")