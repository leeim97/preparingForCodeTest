def solution(x, n):
    answer = []
    x= x
    
    for i in range(n):
        answer.append(x+(x*i))
    
    return answer