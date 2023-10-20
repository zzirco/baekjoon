from collections import deque

n = int(input())
order = deque([])
arr = deque()

for i in range(n):
    string = input().split()
    order.append(string)

for i in range(n):
    if len(order[i]) == 2:
        a, b = order[i]
        if a == "push_front":
            arr.appendleft(b)
        elif a == "push_back":
            arr.append(b)
    else:
        a = order[i][0]
        if a == "pop_front":
            if len(arr) == 0:
                print("-1")
            else:
                print(arr.popleft())
        elif a == "pop_back":
            if len(arr) == 0:
                print("-1")
            else:
                print(arr.pop())
        elif a == "size":
            print(len(arr))
        elif a == "empty":
            if len(arr) == 0:
                print("1")
            else:
                print("0")
        elif a == "front":
            if len(arr) == 0:
                print("-1")
            else:
                print(arr[0])
        elif a == "back":
            if len(arr) == 0:
                print("-1")
            else:
                print(arr[len(arr)-1])