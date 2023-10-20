minus_split_arr = list(input().split('-'))
arr = []
for item in minus_split_arr:
    plus_split_arr = list(map(int, item.split('+')))
    ans = sum(plus_split_arr)
    arr.append(ans)

result = arr[0]

for i in range(1, len(arr)):
    result -= arr[i]
print(result)