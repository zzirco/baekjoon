import sys
from bisect import bisect_right
input = sys.stdin.readline
n = int(input())


def merge(left, right):
    ret = []
    i = j = 0
    l = len(left)
    r = len(right)
    while True:
        if i == l:
            for k in range(j, r):
                ret.append(right[k])
            break
        if j == r:
            for k in range(i, l):
                ret.append(left[k])
            break
        if left[i] < right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1
    return ret


tree = [[]for _ in range(1 << 18)]


def build(arr, s=1, e=n, x=1):
    if s == e:
        tree[x].append(arr[s-1])
        return
    mid = s + e >> 1
    build(arr, s, mid, x << 1)
    build(arr, mid+1, e, x << 1 | 1)
    tree[x] = merge(tree[x << 1], tree[x << 1 | 1])


def query(k, l, r, s=1, e=n, x=1):
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return len(tree[x]) - bisect_right(tree[x], k)
    mid = s + e >> 1
    return query(k, l, r, s, mid, x << 1) + query(k, l, r, mid+1, e, x << 1 | 1)


arr = [*map(int, input().split())]
build(arr)
for _ in range(int(input())):
    i, j, k = map(int, input().split())
    print(query(k, i, j))