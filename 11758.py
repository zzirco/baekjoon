arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

def ccw(arr):
    x1 = arr[0][0]
    x2 = arr[1][0]
    x3 = arr[2][0]
    y1 = arr[0][1]
    y2 = arr[1][1]
    y3 = arr[2][1]
    temp = x1*y2+x2*y3+x3*y1
    temp = temp - y1*x2-y2*x3-y3*x1
    if temp > 0:
        return 1
    elif temp < 0: 
        return -1
    else:
        return 0
    
print(ccw(arr))