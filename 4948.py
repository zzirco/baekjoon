import math

arr = [True for i in range(246913)]

for i in range(2, int(math.sqrt(246912)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= 246912:
            arr[i * j] = False
            j += 1

while True:
    m = int(input())
    if m == 0:
        break
    n = 2 * m
    count = 0
    for i in range(m + 1, n + 1):
        if arr[i]:
            count += 1
    print(count)