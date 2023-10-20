x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(x1, x2, x3, y1, y2, y3):
    temp = x1*y2+x2*y3+x3*y1
    temp = temp - y1*x2-y2*x3-y3*x1
    if temp > 0:
        return 1
    elif temp < 0: 
        return -1
    else:
        return 0
    
if (ccw(x1, x2, x3, y1, y2, y3) * ccw(x1, x2, x4, y1, y2, y4) <= 0) and (ccw(x3, x4, x1, y3, y4, y1) * ccw(x3, x4, x2, y3, y4, y2) <= 0):
    print("1")
else:
    print("0")