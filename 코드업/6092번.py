n= int(input())
a=list(map(int, input().split()))

# for i in range(24):
#     print(a[i],type(a[i]))


d=[0]*24
for i in range(n):
    d[a[i]-1]+=1

for i in range(23):
    print(d[i],end=" ")