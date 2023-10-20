n = int(input())

arr = []
stack = []


for i in range(n):
    arr.append(list(input()))

for i in range(n):
    stack.clear()
    result = False
    for j in range(len(arr[i])):
        s = arr[i][j]
        if s == "(":
            stack.append(s)
        else:
            if len(stack) == 0:
                print("NO")
                result = True
                break
            else:
                stack.pop()
    if result == True:
        continue
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
