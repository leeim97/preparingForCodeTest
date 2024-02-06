n = int(input())
store = list(map(int,input().split()))
store.sort( )

m = int(input())
client = list(map(int,input().split()))

def binary_search(target,store,start,end):
    if start > end:
        return False
    mid=(start+end)//2

    if store[mid] == target:
        return True

    elif store[mid] > target:
        return binary_search(target,store,mid+1,end)
    else:
        return binary_search(target, store, mid + 1, end)

for i in range(m):
    if binary_search(client[i],store,0,n-1) :
        print('yes',end=" ")
    else:
        print('no',end=' ')