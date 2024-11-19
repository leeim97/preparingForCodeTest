import sys
from collections import deque

num = int(input())

for i in range(num):

    M, ind = map(int,sys.stdin.readline().split())
    arr = deque([0]*M)
    arr[ind] = 1

    queue = deque(list(map(int,sys.stdin.readline().split())))

    order = 1


    # print(arr)
    # print(queue)
    while queue:
        # print(arr)
        # print(queue)
        Ma = max(queue)
        temp = queue.popleft()
        if temp == Ma:
            temp2 = arr.popleft()
            if temp2 == 1:
                break
            else:
                order +=1
        else:
            queue.append(temp)
            arr.append(arr.popleft())

    print(order)
