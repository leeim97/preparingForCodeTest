import sys
input = sys.stdin.readline
INF=int(1e9)


print('정점과 간선의 갯수 입력 : ')
v,e = map(int,input().split())
start = int(input())

visited=[False]*(v+1)
distance=[INF]*(v+1)
graph = [[] for i in range(v+1)]

def get_smallest_node():
    min_dist=INF
    index = 0

    for i in range(1,v+1):
        if distance[i] < min_dist and visited[i] == False :
            index = i
            min_dist=distance[i]

    return index

print('정점 두개와 비용 입력 : ')
for _ in range(e):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))

def dijkstra(start):
    visited[start] = True
    distance[start]=0
    for i in graph[start]:
        distance[i[0]] = i[1]

    for j in range(v-1):
        s_node= get_smallest_node()
        visited[s_node]= True
        for k in graph[s_node]:
            if distance[k[0]] > distance[s_node] + k[1]:
                distance[k[0]]= distance[s_node] + k[1]


dijkstra(start)

for i in range(1,v+1):
    print(distance[i])

print(graph)





