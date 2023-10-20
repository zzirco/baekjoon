import sys
input = sys.stdin.readline
cnt = 0

def merge_sort(array):
    global cnt
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j = 0, 0
    tmp = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
            cnt += len(left) - i

    tmp += left[i:]
    tmp += right[j:]

    return tmp

N = int(input())
arr = list(map(int, input().split()))
arr = merge_sort(arr)
print(cnt)