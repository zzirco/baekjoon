arr = list(map(int, input()))
arr.sort(reverse=True)
for i in range(len(arr)):
    print(arr[i], end='')