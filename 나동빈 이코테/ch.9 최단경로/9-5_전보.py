import heapq
import sys

# readline에 ()치면 안됌
input = sys.stdin.readline
INF = 1e9


n,m,start = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance= [INF]*(n+1)

def dijkstra(start):

    q=[]
    # 우선순위를 거리로 할꺼기때문에 0을 앞에 넣어준다
    heapq.heappush(q,(0,start))
    distance[start]=0
    result = 0
    while q:
        cost,now = heapq.heappop(q)

        # 이부분 등호 잘못썻음
        if cost > distance[now]:
            continue
        # i[1]는 비용 ,i[0]은 도착 노드
        for i in graph[now]:
            if distance[i[0]] > cost + i[1]:
                distance[i[0]] = cost + i[1]
                heapq.heappush(q,(distance[i[0]],i[0]))


for i in range(m):
    a,b,cost= map(int,input().split())
    graph[a].append((b,cost))


dijkstra(start)

# 도착 도시 개수
count=0
# 총 결과값(노드 중에 제일 늦게 걸리는 시간 기준 왜냐하면 제일 늦은 노드가 다 되면 그전에 다른 노드들은 이미 끝나있을테니까)
result=0
print(distance)
for i in range(1,n+1):
    if i == start:
        continue
    if distance[i] == INF:
        continue
    else:
        count+=1
        if result < distance[i]:
           result=distance[i]

print(count,result)