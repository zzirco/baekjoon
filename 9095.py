import sys
input = sys.stdin.readline

n = int(input())

cache = [-1] * 12
cache[0] = 0 
cache[1] = 1 
cache[2] = 2 
cache[3] = 4

def fn(a):
    if cache[a] != -1:
        return cache[a]
    for i in range(4, a + 1):
        cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
    return cache[a]

for _ in range(n):
    print(fn(int(input())))