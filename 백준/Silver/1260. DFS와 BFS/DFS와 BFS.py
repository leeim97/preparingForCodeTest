from collections import deque
def dfs(start):
    visit[start] = True
    print(start, end=' ')

    for j in graph[start]:
        if visit[j] == False:
            dfs(j)



def bfs(start):
    visit[start] = True
    q = deque([start])


    while q:
        temp = q.popleft()
        print(temp,end= ' ')
        for j in graph[temp]:
            if visit[j] == False:
                visit[j] = True
                q.append(j)



N,M,start = map(int,input().split())

visit = [False]*(N+1)
graph = [ [] for _ in range(N+1) ]


for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


dfs(start)
print()
visit = [False]*(N+1)
bfs(start)

