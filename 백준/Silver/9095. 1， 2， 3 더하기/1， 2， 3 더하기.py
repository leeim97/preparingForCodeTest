num = int(input())

for i in range(num):
    n = int(input())
    arr = [0]*(n+1)
    if n>=1:
        arr[1]= 1
    if n>=2:
        arr[2]= 2
    if n>=3:
        arr[3]= 4

    for j in range(4,n+1):
        arr[j] = arr[j-1]+arr[j-2]+arr[j-3]

    print(arr[n])