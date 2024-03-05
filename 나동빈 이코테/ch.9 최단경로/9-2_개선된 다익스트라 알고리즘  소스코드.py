import sys
import heapq

input= sys.stdin.readline
INF=int(1e9)

print('정점 간선 개수 입력 : ')
v,e = map(int,input().split())
start=int(input())

distance=[INF]*(v+1)
graph=[[] for _ in range(v+1)]


print('도착노드 비용 입력 : ')
for i in range(e):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost)) # 도착 노드, 비용

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,s_node = heapq.heappop(q)

        if dist > distance[s_node]:
            continue

        for i in graph[s_node]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q,(distance[i[0]],i[0]))

dijkstra(start)
for i in range(1,v+1):
    print(distance[i])


