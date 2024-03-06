INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
n=int(input())
e=int(input())

graph=[[INF] * (n+1) for _ in range(n+1)]
print(graph)

# 자기 자신으로 가는거 비용 0처리
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0



#각 간선에 대한 정보 입력받아, 그 값으로 초기화
for i in range(e):
    a,b,cost = map(int, input().split())
    graph[a][b]=cost

print(graph)
# 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n + 1):
        if k==a:
            continue
        for b in range(1,n + 1):
            if a == b:
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print('a,b',a,b)
for i in range(1,n+1):
    for j in range(1,n+1):
        # print(f'i:{i} j:{j}')
        if graph[i][j]== INF:
            print('무한',end=' ')
        else:
            print(graph[i][j],end= ' ')
    print()
