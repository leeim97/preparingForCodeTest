# N은 집 ,M은 길의 수
N,M = map(int,input().split())
parent = [0]*(N+1)
edges=[]            # 이걸 생각을 못했네 edges는 크루스칼을 쓰기위해 비용 모음

for i in range(N+1):
    parent[i]=i

#최소 신장트리 -> 크루스칼 알고리즘(union,find)
# 마을을 두개로 나눠야한다 -> 가장 효율적인 방법은?

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]

def union(a,b):
    p_a=find_parent(a)
    p_b=find_parent(b)
    if p_a > p_b:
        parent[p_a]=p_b
    elif p_a < p_b:
        parent[p_b]=p_a

def div_uni():
    pass

for i in range(M):
    a,b,cost=map(int,input().split()) # a집에서 #b집으로 연결하는 비용 cost
    edges.append((cost,a,b))          # 분류하기위해서 cost를 맨 앞에

edges.sort()


result=0
last =0         # ★마지막 제일 큰 길 값 넣어둠
for i in edges:
    a,b=i[1],i[2]        # i[index]를 써야되는데 edges[0],edges[1]을 넣어서 튜플이 들어가서 find_parent에서  TypeError가 생겼다.

    if find_parent(a) != find_parent(b):
        union(a,b)
        result+=i[0]
        last=i[0]


print(result-last)