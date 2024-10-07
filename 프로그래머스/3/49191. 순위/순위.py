def solution(n, results):
    answer=0
    board = [[0]*(n+1) for i in range(n+1)]
    
    for re in results:
        board[re[0]][re[1]] = 1
        board[re[1]][re[0]] = -1

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j or board[i][j] in [-1,1]:
                    continue
                    
                # 영희는 철수를 이기고 철수는 기훈이를 이기면 영희는 기훈이를 이김
                elif board[i][k] == board[k][j] ==1:
                    board[i][j]=1
                    
                    #지는 것들을 표기해줘야함
                    board[k][i]  =board[j][k]=board[j][i] = -1
                    
                    
                    
    for i in range(1,n+1):
        #모르는게 한개는 자기 자신과의 승부만을 나타내므로 결국 나머지와 다 결과가 있음
        # 맨앞에 쓰레기값 0까지 포함해서 총 2개
        
        if board[i].count(0) == 2:
            answer+=1
            
    print(board)
    return answer