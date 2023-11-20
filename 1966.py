from collections import deque

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    priority = deque()
    for i in range(n):
        priority.append((arr[i], i))
    index = 0
    cnt = 0
    while(priority):
        if priority[0][0] != max(priority)[0]:
            priority.append(priority.popleft())
        else:
            num = priority.popleft()
            cnt += 1
            if num[1] == m:
                print(cnt)
                break
        index += 1
        