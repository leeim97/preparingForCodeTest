n,m = map(int,input().split())

array= list(map(int,input().split()))

start=0
end=max(array)

result=0

while start<=end:
    mid=(start+end)//2
    total=0
    for i in range(n):
        if array[i] >= mid:
            total+=array[i]-mid

    if total >= m:
        start=mid +1
        result=mid

    elif total <m :
        end=mid-1



print(result)



