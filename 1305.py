n=int(input())
arr=input()

pi=[0 for _ in range(n)]
i=0
for j in range(1,n):
    while i>0 and arr[i]!=arr[j]:
        i=pi[i-1]
    if arr[i]==arr[j]:
        i+=1
        pi[j]=i
i=n-1-pi[n-1]
print(i+1)