n = int(input())
for i in range(n):
    index = int(input())
    arr = []
    arr.append(1)
    arr.append(1)
    arr.append(1)
    for i in range(3, index):
        a = arr[i - 2] + arr[i - 3]
        arr.append(a)
    print(arr[index - 1])
