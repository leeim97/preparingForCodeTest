def solution(a, b):
    answer = 0
    maxo=0
    mino=0
    
    if a>=b:
        maxo = a
        mino = b
    else:
        maxo=b
        mino =a
    for i in range(mino,maxo+1):
        answer+= i
        
    
    return answer