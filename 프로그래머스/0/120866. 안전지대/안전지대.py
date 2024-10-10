def solution(board):
    answer = 0
    n = len(board)
    # 그냥 테두리를 하나씩 더 붙여서 상하좌우 2 추가할때 인덱스 고려 안하게끔
    re = [[0]*(n+2) for _ in range(n+2) ]
    bb = [-1,0,1]
    
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            
            if board[i-1][j-1] == 1:
                for b in bb: 
                    for k in bb:
                        if b==0 and k==0:
                            re[i+b][j+k] =1
                        else:
                            re[i+b][j+k]=2
    
    for i in board:
        print(i)
        
    print('\n')
    for i in re:
        print(i)
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if re[i][j]==0:
                answer+=1
            
    
    
    return answer