N = int(input())
arr1 = list(map(int,input().split()))

M = int(input())
arr2 = list(map(int,input().split()))

arr1.sort()
dic = {}
for i in arr1:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic[i]=1

for j in arr2:
    find = False

    start = 0
    end = len(arr1) - 1

    while start <= end :

        mid = (start + end)//2

        if arr1[mid] == j:
            find = True
            break
        elif arr1[mid] > j:
            end = mid -1
        elif arr1[mid] < j:
            start = mid +1

    if find:
        print(1,end=' ')
    else:
        print(0,end= ' ')
        