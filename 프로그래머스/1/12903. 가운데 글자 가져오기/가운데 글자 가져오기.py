def solution(s):
    if len(s)%2 == 0:
        num = len(s)//2
        answer= s[num-1:num+1]
    else:
        answer= s[len(s)//2]
    
    
    return answer