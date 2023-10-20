import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*2 for _ in range(n)]

for i in range(n):
    for j in range(2):
        if dp[i][j] == 0:
            dp[i][j] = 0
            

