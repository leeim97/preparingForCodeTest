def solution(n):
    answer=''
    la = ['수','박']
    
    for i in range(n):
        answer+=la[i%2]
    
    return answer