def make_sum(array,N,standard):
    result=0
    for i in range(N):
        if array[i] < standard:
            continue
        else:
            result += (array[i]-standard)

    return result

def binary_search(array,start,end,target):
    if start>end:
        return end

    mid=(start+end)//2

    std=make_sum(array,len(array),mid)
    if target == std:
        return mid

    elif target < std:
        return binary_search(array,mid+1,end,target)

    else:
        return binary_search(array, start, mid -1, target)



N, M = map(int,input().split()) #N은 떡 갯수 M은 떡의 총 길이

array = list(map(int,input().split()))
array.sort()
result=binary_search(array,0,max(array),M)
print(result)
