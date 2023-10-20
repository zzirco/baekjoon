import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().split()))
s = int(input().rstrip())

for i in range(len(arr)):
    j = len(arr)
    while True:
        if i == arr.index(max(arr[i:j])):
            break
        else:
            if arr.index(max(arr[i:j])) - i <= s:
                max_index = arr.index(max(arr[i:j]))
                s -= max_index - i
                for k in range(max_index-1, i-1, -1):
                    arr[k], arr[k+1] = arr[k+1], arr[k]
            else:
                j -= 1
print(*arr)