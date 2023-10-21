import heapq
import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(distance, graph, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(distance, graph, c)

count = 0
result = 0
for i in range(1, n + 1):
    if distance[i] == INF or i == c:
        continue
    else:
        count += 1
        if distance[i] > result:
            result = distance[i]

print(count, result)