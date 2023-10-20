from collections import deque

n = int(input())
k = int(input())
apple = []
direction = []
for i in range(k):
    apple.append(list(map(int, input().split())))
l = int(input())
for i in range(l):
    direction.append(list(input().split()))

arr = [[0]*n for _ in range(n)]

for i in range(len(apple)):
    a, b = apple[i]
    arr[a-1][b-1] = 2

d_type = ['U', 'R', 'D', 'L']
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
x = 0
y = 0
d = 'R'
arr[x][y] = 1
q = deque([])
q.append([x,y])

while True:
    add = False

    for i in range(l):
        if count == int(direction[i][0]):
            if direction[i][1] == 'D':
                index = d_type.index(d) + 1
                if index == 4:
                    index = 0
                    d = d_type[index]
                else:
                    d = d_type[index]
            else:
                index = d_type.index(d) - 1
                if index == -1:
                    index = 3
                    d = d_type[index]
                else:
                    d = d_type[index]

    nx = x + dx[d_type.index(d)]
    ny = y + dy[d_type.index(d)]
    q.append([nx, ny])

    if nx<0 or nx>=n or ny<0 or ny>=n or arr[nx][ny] == 1:
        count += 1
        break

    if arr[nx][ny] == 2:
        count += 1
        arr[nx][ny] = 1
        add = True

    else:
        count += 1
        arr[nx][ny] = 1

    x = nx
    y = ny

    if add == False:
        a, b = q.popleft()
        arr[a][b] = 0

print(count)