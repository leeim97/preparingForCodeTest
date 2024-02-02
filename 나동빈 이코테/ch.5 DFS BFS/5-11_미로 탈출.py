from collections import deque
n,m= map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def BFS(graph):
    queue = deque()
    queue.append((0, 0))

    while queue:
        vx, vy = queue.popleft()
        count = graph[vx][vy]
        if vx==n-1 and vy==m-1:
            return print(graph[vx][vy])

        if vx-1>=0 and graph[vx-1][vy] == 1:
            queue.append((vx-1,vy))
            graph[vx - 1][ vy]=count+1

        if vx+1<n and graph[vx + 1] [vy] == 1:
            queue.append((vx + 1, vy))
            graph[vx + 1] [vy]=count+1

        if vy-1>=0 and graph[vx ][ vy-1] == 1:
            queue.append((vx,vy-1))
            graph[vx][ vy - 1]=count+1

        if vy+1 <m and graph[vx][ vy+1] == 1:
            queue.append((vx, vy +1))
            graph[vx][ vy + 1]=count+1



BFS(graph)
print(graph)