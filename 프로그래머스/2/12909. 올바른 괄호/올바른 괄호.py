from collections import deque
def solution(s):
    
    stack = []
    
    for i in s:
        if i =='(':
            stack.append(i)
        elif i ==')':
            if stack == []:
                return False
            stack.pop()
    
    
    return stack == []