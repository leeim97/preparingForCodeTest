def solution(common):
    answer = 0
    
    d1 = common[1] - common[0]
    d2 = common[2] - common[1]
    
    # 등차수열
    if d1 == d2 : 
        answer = common[-1]+d1
    
    else:
        d3 = common[1] // common[0]
        answer = common[-1]*d3
        
    return answer