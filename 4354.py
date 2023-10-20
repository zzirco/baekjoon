while True:
    arr=input()
    if arr == '.':
        break
    pi=[0 for _ in range(len(arr))]
    i=0
    for j in range(1,len(arr)):
        while i>0 and arr[i]!=arr[j]:
            i=pi[i-1]
        if arr[i]==arr[j]:
            i+=1
            pi[j]=i
    if pi[len(arr) - 1] == 0:
        print("1")
    else:
        if len(arr) % (len(arr) - pi[len(arr) - 1]) == 0:
            print(int(len(arr) / (len(arr) - pi[len(arr) - 1])))
        else:
            print("1")