def remove_not_selfnum(a):
    global selfnumber
    arr = list(map(int, a))
    result = sum(arr) + int(a)
    if result in selfnumber:
        selfnumber.remove(result)
    return

selfnumber = []

for i in range(1, 10001):
    selfnumber.append(i)

for j in range(1, 10001):
    remove_not_selfnum(str(j))

for num in selfnumber:
    print(num)