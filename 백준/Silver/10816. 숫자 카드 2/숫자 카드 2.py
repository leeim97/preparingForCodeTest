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

for i in arr1:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

# print(dic)
for j in arr2:
    print(dic.get(j,0),end = ' ')
