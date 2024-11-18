from collections import deque
import sys

num = int(input())
queue = deque()

for i in range(num):
    sen = sys.stdin.readline().split()
    if sen[0] == 'push_front':
        queue.appendleft(sen[1])
    elif sen[0] == 'push_back':
        queue.append(sen[1])
    elif sen[0] == 'pop_front':
        if len(queue) >= 1 :
            print(queue.popleft())
        else:
            print(-1)
    elif sen[0] == 'pop_back':
        if len(queue) >= 1 :
            print(queue.pop())
        else:
            print(-1)
    elif sen[0] == 'size':
        print(len(queue))
    elif sen[0] == 'empty':
        if len(queue) >=1:
            print(0)
        else:
            print(1)
    elif sen[0] == 'front':
        if len(queue) >= 1:
            print(queue[0])
        else:
            print(-1)
    elif sen[0] == 'back':
        if len(queue) >= 1:
            print(queue[-1])
        else:
            print(-1)
