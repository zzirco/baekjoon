n = int(input())
time = list(map(int, input().split()))

time.sort()

arr = []

for i in range(1, n + 1):
    a = time[0:i]
    ans = sum(a)
    arr.append(ans)

result = sum(arr)
print(result)