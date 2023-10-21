import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def binary_search(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2
        length = 0
        for i in range(n):
            if arr[i] > mid:
                length += (arr[i] - mid)
        print(length)
        if length == key:
            return mid
        elif length > key:
            start = mid + 1
        else:
            end = mid - 1
    return None

result = binary_search(arr, m, 0, arr[n - 1])
print(result)