n = int(input())
order_arr = []
for i in range(n):
    order_arr.append(list(input().split()))

num_arr = []

for i in range(n):
    if order_arr[i][0] == "push":
        num_arr.append(order_arr[i][1])
    elif order_arr[i][0] == "pop":
        if len(num_arr) != 0:
            print(num_arr.pop())
        else:
            print("-1")
    elif order_arr[i][0] == "size":
        print(len(num_arr))
    elif order_arr[i][0] == "empty":
        if len(num_arr) != 0:
            print("0")
        else:
            print("1")
    else:
        if len(num_arr) != 0:
            print(num_arr[len(num_arr) - 1])
        else:
            print("-1")