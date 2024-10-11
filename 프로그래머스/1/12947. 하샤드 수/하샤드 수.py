def solution(x):
    answer = False
    
    num=sum(list(map(int,list(str(x)))))
    
    if x%num==0:
        answer = True
    
    
    
    return answer