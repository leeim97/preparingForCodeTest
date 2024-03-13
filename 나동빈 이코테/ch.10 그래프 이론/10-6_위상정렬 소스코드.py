from collections import deque

v,e = map(int,input().split())
graph=[[] for _ in range(v+1)]
indegree=[0 for _ in range(v+1)]

for i in range(e):
    a,b= map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1


def topology_sort():
    result=[]
    q=deque()               #deque에 ()를 안씀
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:    #now를 i로 씀 바보..
            indegree[i]-=1
            if indegree[i] == 0:
                q.append(i)


    for i in result:             #여기서 result의 index out of range 오류걸렸었음
        print(i,end=" ")

topology_sort()