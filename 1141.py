import time
st = time.time()

n = int(input())

dice = list(map(int, input().split()))

d1 = min(dice)
d2 = min([dice[i] + dice[j] for i in range(6) for j in range(i + 1, 6) if i + j != 5])
d3 = min([dice[i] + dice[j] + dice[k] for i in range(6) for j in range(i + 1, 6) for k in range(j + 1, 6) if i + j != 5 and j + k != 5 and k + i != 5])

result = 0

if n == 1:
    dice.sort()
    for i in range(5):
        result += dice[i]
else:
    result = (d3 * 4) + (d2 * 4 * (n - 1)) + (d2 * 4 * (n - 2)) + (d1 * 4 * (n - 1) * (n - 2)) + (d1 * (n - 2) * (n - 2))

print(result)

et = time.time()
print("시간:", et - st)