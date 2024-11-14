num = int(input())

for i in range(num):
    n, p = input().split()
    # print(type(n),p)
    arr = list(n)
    # print(arr)
    arr2 = list(map(int,arr))
    # print(type(arr[0]), type(arr2[0]))


    for j in range(0,int(p)):
        if j >= len(arr2)-1:
            break
        max = arr2[j]
        ind = j
        for k in range(j+1,len(arr2)):
            if arr2[k]>= max :
                ind = k
                max = arr2[k]

        temp = arr2[j]
        arr2[j] = max
        arr2[ind] = temp
    #print(arr2)
    arr2 = list(map(str,arr2))
    print(f'#{i+1} {"".join(arr2)}')




