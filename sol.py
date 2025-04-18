from collections import deque

def bfs(a,b):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue = deque([(a,b)])

    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <1 or ny <1 or nx >N or ny > M :
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] +1





N,M = map(int,input().split())

graph = [ [0]*(M+1) for _ in range(N+1) ]

for i in range(1,N+1):
    temp_list = map(int,list(input()))
    graph[i][1:] = temp_list

bfs(1,1)
print(graph[N][M])