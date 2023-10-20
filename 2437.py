n = int(input())
weights = list(map(int, input().split()))
weights.sort()
acc = 0
for i in range(n):
    if acc + 1 >= weights[i] :
        acc += weights[i]
    else:
        break
print(acc + 1)