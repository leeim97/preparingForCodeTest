import heapq

#N 회사의 개수 , M 간선의 갯수
n,m = map(int,input().split())

INF = int(1e9)
graph= [[] for _ in range(n+1)]  # [0]넣어서 밑에 두개 가져와야되는 부분 오류나옴
distance=[ INF ] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    cost=1
    # ★★★★★★★★★양방향 주의!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    graph[a].append((b,cost))
    graph[b].append((a, cost))
# print(graph)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        # print(cost,now)

        if distance[now] < cost:
            continue

        else:
            # i[0]은 노드 , i[1]은 거리
            for i in graph[now]:
                print(i)
                # 이 부분이 잘 생각이 안났음, 거리 조절 비교

                if distance[i[0]] > cost + i[1]:
                    distance[i[0]] = cost + i[1]
                    heapq.heappush(q, (distance[i[0]], i[0]))


# K회사 거쳐서 X 회사를 가야함
x,k= map(int,input().split())


dijkstra(1)
# 1번에서 k로의 최단경로
dist_k = distance[k]

# k에서 x거리 다시 재야하니까 distance 초기화
distance=[ INF ] * (n+1)

# x,k 문제 순서대로 안가고 바꿔서 가서 해멤
dijkstra(k)
dist_x = distance[x]

if dist_k == INF:
    print('-1')
else:
    print(dist_x + dist_k)
