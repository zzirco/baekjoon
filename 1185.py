n, k = map(int, input().split())
q = []
for i in range(n):
    q.append(i + 1)

arr = []
arr_index = 0
cnt = 1

while(q):
    if arr_index > (len(q) - 1):
        arr_index = 0
    if cnt == k:
        arr.append(q[arr_index])
        q.remove(q[arr_index])
        cnt = 1
    else:
        arr_index += 1
        cnt += 1

print("<", end = '')
for i in range(n):
    if i != n - 1:
        print(arr[i], end = ', ')
    else:
        print(arr[i], end = '')
print(">")