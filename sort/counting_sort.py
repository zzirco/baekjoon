import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

n = max(arr)
array = [0 for _ in range(n + 1)]

for i in range(len(arr)):
    array[arr[i]] += 1

for i in range(n + 1):
    for j in range(array[i]):
        print(i, end = ' ')