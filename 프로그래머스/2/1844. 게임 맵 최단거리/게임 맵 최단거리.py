from collections import deque
# 0은 벽이 있는 자리, 1은 벽이 없는 자리
# BFS로 풀기

def solution(maps):
    answer = 0
    def BFS(x,y):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        queue = deque()
        queue.append((x,y))
        
        while queue:
            x,y = queue.popleft()

            for i in range(4):
                nx = x+ dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or ny> (len(maps[0])-1) or nx> (len(maps)-1):
                    continue
                    
                elif maps[nx][ny] == 0:
                    continue
                    
                elif maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] +1 
                    queue.append((nx,ny))

        return maps[len(maps)-1][len(maps[0])-1]

    answer = BFS(0,0)
    # 마지막은 항상 -1 이니까 도착하지 않으면 -1 이겠지?
    return -1 if answer == 1 else answer