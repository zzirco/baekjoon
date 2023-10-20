arr = list(input())
array = []
for i in range(len(arr)):
    array.append(arr[-(i + 1):])
array.sort()
for i in range(len(array)):
    print(*array[i], sep='', end='')
    print()