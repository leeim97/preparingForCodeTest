from  collections import deque

queue=deque()

queue.append(1)
queue.append(3)
queue.append(4)
queue.popleft()
queue.append(54)

print(queue)