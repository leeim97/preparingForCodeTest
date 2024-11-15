import sys
from collections import deque

num = int(input())
queue = deque([ i for i in range(1,num+1)  ])

# print(queue)


while len(queue)>1:

    # if len(queue) == 1:
    #     break
    queue.popleft()

    # if len(queue) == 1:
    #     break
    queue.append(queue.popleft())

# print(queue)
print(queue[0])