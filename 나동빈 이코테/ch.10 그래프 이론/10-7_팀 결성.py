# 학생들에게 0~N 개의 번호 부여, M개의 연산
N,M= map(int,input().split())
parent = [0] * (N+1)

for i in range(1,N+1):
    parent[i]=i
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])  #아직 이부분이 조금 생각할때 삐걱댐

    return parent[x]


def union_parent(a,b):
    p_a= find_parent(a)
    p_b= find_parent(b)
    if p_a> p_b:
        parent[p_a]=p_b
    elif p_a < p_b:
        parent[p_b]=p_a

def check_parent(a,b):
    p_a = find_parent(a)
    p_b = find_parent(b)
    if p_a == p_b:
        print('YES')
    else:
        print('NO')

for i in range(M):
    num,a,b = map(int,input().split())
    if num == 0:
        union_parent(a,b)
    elif num ==1:
        check_parent(a,b)
