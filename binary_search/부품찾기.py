import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
key = list(map(int, input().split()))

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

for i in range(m):
    result = binary_search(arr, key[i], 0, n - 1)
    if result == None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')