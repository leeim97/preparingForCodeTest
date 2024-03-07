def find_parent(parent,x):
    if parent[x] !=x:
        return find_parent(parent,parent[x])
    else:
        return x

def union(parent,a,b):
    if find_parent(parent,a) != find_parent(parent,b):
        parent_a= find_parent(parent,a)
        parent_b=find_parent(parent,b)
        if parent_a > parent_b:
            parent[parent_a] = parent_b
        elif parent_a < parent_b:
            parent[parent_b] = parent_a
    else:
        print('사이클 발생')
        return

v,e = map(int,input().split())
parent=[0 for _ in range(v+1)]

print(parent)
for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b=map(int,input().split())
    union(parent,a,b)

print('각 원소가 속한 집합 : ')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()

print('부모 테이블')
for i in range(1,v+1):
    print(parent[i],end=' ')
