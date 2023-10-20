n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


max_weight = 0
max_height = 0
number = [1 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            number[i] += 1
        elif (arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]) or (arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]):
            continue
        elif arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            number[j] += 1

for i in range(n):
    print(number[i], end = ' ')