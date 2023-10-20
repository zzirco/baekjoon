import sys
input = sys.stdin.readline

n = int(input())
arr1 = []
for i in range(n):
    arr1.append(input().rstrip())

arr2 = list(set(arr1))
array = []
for i in range(len(arr2)):
    array.append([len(arr2[i]),arr2[i]])

array.sort()
for i in range(len(array)):
    print(array[i][1])