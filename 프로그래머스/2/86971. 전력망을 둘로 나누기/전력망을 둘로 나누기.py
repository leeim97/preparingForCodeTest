def find_parent(a, parent):
    if parent[a] != a:
        parent[a] = find_parent(parent[a], parent)
    return parent[a]

def union(a, b, parent):
    a_root = find_parent(a, parent)
    b_root = find_parent(b, parent)
    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root

def calculate_difference(parent, n):
    from collections import Counter
    # 각 노드의 최종 부모를 찾습니다.
    root_parents = [find_parent(i, parent) for i in range(1, n+1)]
    count = Counter(root_parents)
    if len(count) != 2:
        # 두 그룹으로 정확히 나뉘지 않았을 경우, 큰 차이를 반환
        return max(count.values()) - min(count.values())
    else:
        groups = list(count.values())
        return abs(groups[0] - groups[1])

def solution(n, wires):
    answer = float('inf')  # 최소 차이를 찾으므로 초기값을 무한대로 설정
    for i in range(len(wires)):
        parent = list(range(n+1))  # 부모 배열을 초기화
        for j in range(len(wires)):
            if i == j:
                continue  # 현재 제거할 wire는 제외
            a, b = wires[j]
            union(a, b, parent)
        diff = calculate_difference(parent, n)
        answer = min(answer, diff)
    return answer