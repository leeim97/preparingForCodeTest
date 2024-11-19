import sys
import heapq

num = int(input())
queue = []

for i in range(num):
    n = int(sys.stdin.readline())

    if n == 0:
        if len(queue) == 0:
            print(0)
        else:
            s = heapq.heappop(queue)
            print(-s)
    else:
        heapq.heappush(queue,-n)



