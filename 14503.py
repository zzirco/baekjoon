n ,m = map(int, input().split())
x, y, d = map(int, input().split())

data = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data.append(list(map(int, input().split())))

count = 0

while True:
    if data[x][y] == 0: #1 현재 칸이 청소되지 않았다면 청소한다
        data[x][y] = 2 #청소한 구역은 2, 청소되지 않은 구역은 0, 벽은 1
        count += 1 #청소 카운트 증가
        if data[x-1][y] != 0 and data[x+1][y] != 0 and data[x][y-1] != 0 and data[x][y+1] != 0: #2 네방향중 청소하지 않은 공간이 없다면
            if data[x-dx[d]][y-dy[d]] != 1: #2-1 바라보는 방향을 유지한채로 후진할 수 있다면 후진하고 1번으로 돌아간다.
                x = x-dx[d]
                y = y-dy[d]
            else: #2-2 후진할 수 없다면 작동을 멈춘다.
                break
        else: #3 네방향중 청소하지 않은 공간이 있다면
            d -= 1 #3-1 반시계 방향으로 90도 회전하고
            if d == -1:
                d = 3
            if data[x+dx[d]][y+dy[d]] == 0: # 3-2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸인 경우 한칸 전진하고 1번으로 돌아간다
                x = x+dx[d]
                y = y+dy[d]
    else: # 현재칸이 청소 된 경우 2번부터 동작한다
        if data[x-1][y] != 0 and data[x+1][y] != 0 and data[x][y-1] != 0 and data[x][y+1] != 0: #2 네방향중 청소하지 않은 공간이 없다면
            if data[x-dx[d]][y-dy[d]] != 1: #2-1 바라보는 방향을 유지한채로 후진할 수 있다면 후진하고 1번으로 돌아간다.
                x = x-dx[d]
                y = y-dy[d]
            else: #2-2 후진할 수 없다면 작동을 멈춘다.
                break
        else: #3 네방향중 청소하지 않은 공간이 있다면
            d -= 1 #3-1 반시계 방향으로 90도 회전하고
            if d == -1:
                d = 3
            if data[x+dx[d]][y+dy[d]] == 0: # 3-2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸인 경우 한칸 전진하고 1번으로 돌아간다
                x = x+dx[d]
                y = y+dy[d]

print(count)