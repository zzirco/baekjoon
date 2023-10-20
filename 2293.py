n, k = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [0] * (k + 1)

for i in range(n):
    if array[i] > k:
        continue
    d[array[i]] += 1
    for j in range(array[i] + 1, k + 1):
        d[j] += d[j - array[i]]

print(d[k])