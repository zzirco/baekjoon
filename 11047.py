n, k = map(int,input().split())

coin = []

for i in range(n):
    coin.append(int(input()))

count = 0
i = 1

while k != 0:
    if coin[n-i] <= k:
        count += k // coin[n-i]
        rest = k % coin[n-i]
        k = rest
        i += 1
    else:
        i += 1

print(count)