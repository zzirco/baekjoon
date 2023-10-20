from collections import deque

n = int(input())

graph = []
danji = []

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(start):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque([start])
    graph[start[0]][start[1]] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n or graph[nx][ny] == 0:
                continue
            else:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                count += 1
    
    danji.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        else:
            bfs([i,j])

danji.sort()
print(len(danji))

for i in danji:
    print(i)