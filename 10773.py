k = int(input())
arr=[]

for i in range(k):
    a = int(input())
    if a != 0:
        arr.append(a)
    else:
        arr.pop()

print(sum(arr))