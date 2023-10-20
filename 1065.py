n = int(input())
count = 0
for i in range(1, n + 1):
    if i < 100:
        count += 1
    elif 100 <= i < 1000:
        num = str(i)
        if int(num[1]) - int(num[0]) == int(num[2]) - int(num[1]):
            count += 1
print(count)