import sys
input = sys.stdin.readline

def binary_search(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
cmp = list(map(int, input().split()))
arr.sort()

for i in range(m):
    result = binary_search(arr, cmp[i], 0, n - 1)
    if result != None:
        print("1", end = ' ')
    else:
        print("0", end = ' ')