import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))

arr.sort()
cnt = 0
vlg = 1
for i in range(m):
    if arr[i][0] == vlg and (cnt + arr[i][2]) <= c:
        cnt += arr[i][2]

