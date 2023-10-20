n = int(input())

i = 1
count = 0
reverse = True
finished = False

while True:
    slice_arr = []
    for item in range(1, i + 1):
        slice_arr.append(item)

    length = len(slice_arr)

    if reverse == True:
        slice_arr.reverse()

    for j in range(len(slice_arr)):
        count += 1
        if count == n:
            first = slice_arr[j]
            second = slice_arr[length-j-1]
            print(first, '/', second)
            finished = True
            break

    reverse = not(reverse)

    if finished == True:
        break

    i += 1