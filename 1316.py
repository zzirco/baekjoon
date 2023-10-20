num = int(input())
res = 0

for i in range(num):
    word = input()
    count = 0
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            if word[j+1:].count(word[j]) > 0:
                count += 1
    if count == 0:
        res += 1

print(res)