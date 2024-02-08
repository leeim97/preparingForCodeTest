n,m=map(int,input().split()) #n은 화폐종류 m은 금액

array=[]
for i in range(n):
    array.append(int(input()))

INF=10001
d=[INF]*(m+1)

d[0]=0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != INF:
            d[j]=min(d[j],d[j-array[i]]+1)


if d[m]==INF:
    print(-1)
else:
    print(d[m])