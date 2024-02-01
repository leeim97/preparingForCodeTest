def DFS(graph,n,visited):
    visited[n]=True
    print(n,end=' ')

    for i in graph[n]:
        if visited[i] == False:
            DFS(graph,i,visited)




graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9

print(DFS(graph,1,visited))
