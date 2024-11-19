num = int(input())

arr = [-1]*(num +1)

arr[1]=0
if num >=2:
    arr[2] = 1
if num >=3:
    arr[3] = 1

if num<=3:
    print(arr[num])
else:
    for i in range(4,num+1):
        arr[i] = arr[i-1] +1
        if i%3 == 0:
            arr[i]= min(arr[i//3] +1, arr[i])
        if i%2 ==0:
            arr[i] = min(arr[i//2] +1, arr[i])


    # print(arr[:num+1])
    print(arr[num])




