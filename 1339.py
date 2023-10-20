n = int(input())

arr = []

for i in range(n):
    arr.append(input())

max_len = 0

for i in range(n):
    if max_len < len(arr[i]):
        max_len = len(arr[i])
        max_index = i

list = list(arr[max_index])

list[0].replace(9)

print(list[0])