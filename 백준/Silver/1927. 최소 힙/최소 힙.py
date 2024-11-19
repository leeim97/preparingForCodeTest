import sys
import heapq

num= int(input())

queue = []
for i in range(num):
    val = int(sys.stdin.readline().rstrip())
    # print(val,type(val))
    if val == 0:
        if len(queue)== 0:
            print(0)
        else:
            print(heapq.heappop(queue))
    else:
        heapq.heappush(queue,val)
