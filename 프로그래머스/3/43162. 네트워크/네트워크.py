def solution(n, computers):
    answer = 0
    
    parent = [0] * len(computers[0])
    print(parent)
    for i in range(len(parent)):
        parent[i] = i
    print(parent)
    
    def find_parent(parent,a):
        if parent[a] != a:
            parent[a] = find_parent(parent,parent[a])
            
        return parent[a]
    
    def union(parent,a,b):
        ra = find_parent(parent,a)  
        rb = find_parent(parent,b)
        if ra > rb:
            parent[ra]= parent[rb]
        else:
            parent[rb]= parent[ra]
            
    for i in range(len(computers[0])):
        for j in range(len(computers[0])):
            print(i,j)
            if i==j:
                continue
                
            if computers[i][j] == 1:
                if find_parent(parent,i) != find_parent(parent,j):
                    union(parent,i,j)
                
    for i in range(n):
        parent[i] = find_parent(parent, i)
        
    cnt =0
    cnt = len(list(set(parent)))
    print(parent)
    return cnt