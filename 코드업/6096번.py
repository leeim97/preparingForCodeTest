d=[[0]*19 for _ in range(19)]


for i in range(19):
    d[i]= list(map(int,input().split()))

# for i in range(19):
#     for j in range(19):
#         print(d[i][j],end="")
#
#     print()


n=int(input())
k=1
while k<=n:
    x,y=map(int,input().split())

    for i in range(19):
        if d[i][y-1]==0:
            d[i][y-1]=1
        elif d[i][y-1]==1:
            d[i][y-1]=0

    for i in range(19):
        if d[x-1][i]==0:
            d[x-1][i]=1
        elif d[x-1][i]==1:
            d[x-1][i]=0
    k+=1

for i in range(19):
    for j in range(19):
        print(d[i][j],end=" ")

    print()