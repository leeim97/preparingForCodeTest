arr= [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    if len(arr)<=1: #len(arr) == 1하니까 안됌 반면에 ==0은 또 됌
        # 왜냐하면 0,1남았을때 왼쪽에는 아무것도 안들어가고 오른쪽에는 1들어가니까 아무것도 안들어갔을경우는 len==0이니까 이 부분도 처리해야됌
        return arr

    pivot=arr[0]
    tails=arr[1:]

    left_side = [x for x in tails if x < pivot ]
    right_side=[ x for x in tails if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

arr=quick_sort(arr)
print(arr)