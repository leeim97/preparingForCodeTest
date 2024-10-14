# cnt = 0으로 초기화 하지 않는 이유는 부모cnt는 자식 cnt에 영향을 안받으니까!!

def dfs(k, cnt, dungeons, visited):
    global answer  # 전역 변수 선언
    
    # 가장 높은 탐험 횟수를 저장
    if answer < cnt:
        answer = cnt
    
    # 모든 던전에 대해 탐험 여부 확인
    for i, v in enumerate(dungeons):
        if k >= v[0] and not visited[i]:  # 던전 진입 조건 (필요 피로도 충족 및 방문하지 않았을 경우)
            visited[i] = True
            dfs(k - v[1], cnt + 1, dungeons, visited)  # 피로도 소모 및 카운트 증가
            visited[i] = False  # 백트래킹 (다음 시도를 위해 방문 여부 초기화)

def solution(k, dungeons):
    global answer
    answer = 0
    visited = [False] * len(dungeons)  # 방문 여부를 저장하는 리스트
    dfs(k, 0, dungeons, visited)
    
    return answer
