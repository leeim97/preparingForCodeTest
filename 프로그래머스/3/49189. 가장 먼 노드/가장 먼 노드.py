import heapq
def solution(n, edge):
    answer = 0
    
    INF = 999999999
    
    distance = [INF]*(n+1)
    graph = [[] for _ in range(n+1)]
    
    for ed in edge:
        i= ed[0]
        j= ed[1]
        graph[i].append((1,j))
        graph[j].append((1,i))
    
    def dijkstra(start):
        q = []
        distance[start] = 0
        # 처음이 cost 두번째가 vertex
        heapq.heappush(q,(0,start))

        while q : 
            
            dist, now = heapq.heappop(q)
            # 처리가 된 적 있으면 생략
            if distance[now] < dist:
                continue

            for v in graph[now]:
                cost = dist + v[0]
                if cost < distance[v[1]]:
                    distance[v[1]] = cost
                    heapq.heappush(q,(cost,v[1]))
    
    dijkstra(1)
    print(distance)
    
    # 맨 처음 의미없는거는 INF니까 0으로 맞춤
    distance[0] = 0
    max_num = max(distance)
    
    for i in distance:
        if i == max_num:
            answer+=1
    
    return answer


        
    
    