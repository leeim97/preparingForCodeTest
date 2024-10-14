def solution(brown, yellow):
    # n은 가로 m은 세로
    answer = []
    
    for i in range(1,yellow+brown):
        if yellow % i ==0:
            n=i
            m= yellow/i
        
            if 2*(n+m+2) == brown:
                answer.append(m+2)
                answer.append(n+2)
                
                break
    
    return answer