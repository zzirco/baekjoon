import copy
import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = []

for i in range(n):
    graph.append(list(input()))

graph2 = copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if graph2[i][j] == "R" or graph2[i][j] == "G":
            graph2[i][j] = "S"

def dfs(arr, x,y,rgb):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if arr[x][y] == rgb:
        arr[x][y] = "v"
        dfs(arr, x - 1, y, rgb)
        dfs(arr, x + 1, y, rgb)
        dfs(arr, x, y - 1, rgb)
        dfs(arr, x, y + 1, rgb)
        return True
    return False

result = 0
result2 = 0

for i in range(n):
    for j in range(n):
        if dfs(graph, i, j, "R") == True:
            result += 1
        if dfs(graph, i, j, "G") == True:
            result += 1
        if dfs(graph, i, j, "B") == True:
            result += 1
        if dfs(graph2, i, j, "S") == True:
            result2 += 1
        if dfs(graph2, i, j, "B") == True:
            result2 += 1

print(result, result2)