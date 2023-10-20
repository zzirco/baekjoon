from math import pi

n, l = map(int, input().split())
dots=[]
for i in range(n):
    x, y = map(int, input().split())
    dots.append((x,y))

def dist(x1,y1,x2,y2) :
    return (y2-y1)**2 + (x2-x1)**2

def ccw(p1,p2,p3):
    return p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1])

def find_Convex_Hull(dots):
    dots.sort()
    lower=[]
    for d in dots:
        while len(lower)>=2 and ccw(lower[-2],lower[-1],d)<=0:
            lower.pop()
        lower.append(d)
    upper=[]
    for d in reversed(dots):
        while len(upper)>=2 and ccw(upper[-2],upper[-1],d)<=0:
            upper.pop()
        upper.append(d)
    return lower[:-1]+upper[:-1]

convexhull=find_Convex_Hull(dots)
res = 0

for i in range(len(convexhull)) :
    if i == len(convexhull) - 1:
        a, b = convexhull[i], convexhull[0]
    else:
        a, b = convexhull[i], convexhull[i+1]
    res += dist(*a,*b)**0.5
res += 2*pi*l
print(round(res))