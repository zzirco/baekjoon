data = []

for i in range(10):
    data.append([])
    for j in range(10):
        data[i].append(0)

for i in range(10):
    a = list(map(int, input().split()))
    for j in range(10):
        data[i][j] = a[j]

global x
global y
x=1
y=1

while data[x][y]!=2:
    if data[x][y]==0:    #현재 위치가 0이면
        data[x][y]=9     #9로 바꾸고 오른쪽으로 계속 진행
        y = y + 1
    else:                #현재 위치가 1이면
        if data[x+1][y-1]==0:     #대각선 왼쪽 아래 위치가 0이면
            data[x+1][y-1]=9    #9로 바꾸고 오른쪽으로 계속 진행
            x = x + 1
        elif data[x+1][y-1]==2:
            data[x+1][y-1]=9
            break
        else:
            break
        
if data[x][y]==2:    
    data[x][y]=9

for i in range(10):
    for j in range(10):
        print(data[i][j], end = ' ')
    print()