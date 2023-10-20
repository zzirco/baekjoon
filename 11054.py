n = int(input())
sequence = list(map(int, input().split()))

up_dp = [1] * n
down_dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            if up_dp[i] < up_dp[j] + 1:
                up_dp[i] = up_dp[j] + 1

for i in range(2, n+1):
    for j in range(1, i):
        if sequence[-i] > sequence[-j]:
            if down_dp[-i] < down_dp[-j] + 1:
                down_dp[-i] = down_dp[-j] + 1
    up_dp[n-i] += down_dp[-i]-1

print(max(up_dp))