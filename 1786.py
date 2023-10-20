def kmp(arr, pattern):
    pi=[0 for _ in range(len(pattern))]
    i=0
    for j in range(1,len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = pi[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            pi[j] = i

    result = []
    i = 0
    for j in range(len(arr)):
        while i > 0 and pattern[i] != arr[j]:
            i = pi[i - 1]
        if pattern[i] == arr[j]:
            i += 1
            if i == len(pattern):
                result.append(j - i + 2)
                i = pi[i - 1]

    return result

arr = input()
pattern = input()
print(len(kmp(arr, pattern)))
print(*kmp(arr, pattern), end=' ')