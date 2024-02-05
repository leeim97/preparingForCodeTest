n= int(input())

arr=[]

for i in range(n):
    data=input().split()
    arr.append([data[0],int(data[1])])

arr= sorted(arr,key=lambda data:data[1])



for i in range(len(arr)):
    print(arr[i][0],end=' ')
