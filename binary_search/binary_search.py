import sys
input = sys.stdin.readline

n, key = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr, key, start, end):
    if start > end:
        return None
    mid = int((start + end) / 2)
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, end)
    
result = binary_search(arr, key, 0, n - 1)
if result == None:
    print("None")
else:
    print(result+1)