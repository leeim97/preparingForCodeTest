def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])

    return parent[x]
def union(parent,a,b):
    p_a=find_parent(parent,a)
    p_b=find_parent(parent,b)
    if p_a < p_b:
        parent[p_b]=p_a
    else:
        parent[p_a] = p_b

v,e = map(int,input().split())
parent=[0 for _ in range(v+1)]
edges=[]
result= 0

for i in range(v+1):
    parent[i]=i

for i in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()


for edge in edges:
    a=edge[1]
    b=edge[2]
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent,a,b)
        result+=edge[0]

print(result)
