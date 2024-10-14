from collections import deque


    
def solution(n, wires):
    answer = 999999999
    visited = [False for _ in range(n+1)]
    graph = [ [] for _ in range(n+1) ]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    
    def bfs(start, visited):
        queue = deque([start])

        visited[start] = True
        cnt = 1

        while queue:
            v = queue.popleft()
            for i in graph[v] : 
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    cnt +=1
        return cnt
    
    
        

    for i,j in wires:
        graph[i].remove(j)
        graph[j].remove(i)

        a= bfs(i,visited)
        visited = [False for _ in range(n+1)]
        b= bfs(j,visited)
        visited = [False for _ in range(n+1)]
        answer = min(abs(a-b),answer)
        
        graph[i].append(j)
        graph[j].append(i)

    print(graph)
    
    return answer