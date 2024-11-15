import sys
from collections import deque

num = int(input())
queue = deque()

for _ in range(num):
    a = sys.stdin.readline().split()
    # print(a[0:4])



    if a[0] == 'push':
        X = a[1]
        queue.append(X)
    elif a[0] == 'pop':
        if len(queue) ==0:
            print(-1)
            continue
        else:
            print(queue.popleft())
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[0])
    elif a[0] == 'back':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[-1])