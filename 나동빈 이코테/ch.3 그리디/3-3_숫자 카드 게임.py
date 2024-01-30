N,M= map(int,input().split())

arr = [[0]*M for _ in range(N)]

for i in range(N):
    arr[i]=list(map(int,input().split()))

max=0
for i in range(N):
    if max < min(arr[i]):
        max=i

print(min(arr[i]))

