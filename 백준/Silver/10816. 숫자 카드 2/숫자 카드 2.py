# dict의 get메소드 
# dic.get(key,value)
# key에 해당하는거 찾아줌 없으면 value 반환 value 안쓰면 None 반환

import sys

num = int(input())

arr1 = list(map(int,sys.stdin.readline().split()))

num2 = int(input())

arr2 = list(map(int,sys.stdin.readline().split()))

arr1.sort()

dic = {}

# 틀린 답안
# for i in set(arr1):
#     dic[i] = arr1.count(i)

# 이 방법 생각을 못했네 O(n)을써서 개수 구하는거
for i in arr1:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1


# 찾기
# 이것도됌
# for j in arr2:
#     print(dic.get(j,0),end = ' ')


for j in arr2:
    start = 0
    end = len(arr1)-1

    while start <= end:
        mid = (start + end)//2

        if arr1[mid] == j:
            print(dic[j])
            break

        elif arr1[mid] > j:
            end = mid -1

        elif arr1[mid] < j:
            start = mid +1

    if start > end:
        print(0)
