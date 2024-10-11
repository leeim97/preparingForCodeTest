def solution(s):
    answer = True
    
    a= s.count('P') + s.count('p')
    b= s.count('y') + s.count('Y')
    if a==b:
        return True
    else:
        return False

    return True