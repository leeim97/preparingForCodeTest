def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2

    if array[mid]== target:
        return mid+1

    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    elif array[mid] < target:
        return binary_search(array,target,mid+1,end)

n,target = map(int,input().split())
array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1)

if result == None:
    print("원소가 없습니다.")
else:
    print(result)
