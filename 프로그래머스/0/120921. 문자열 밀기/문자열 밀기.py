from collections import deque

def solution(A, B):
    queue= deque(A)
    print(''.join(list(queue)))
    answer = 0
    
    a=A
    for i in range(len(A)) :
        
        if a==B:
            return answer
        f = queue.pop()
        queue.appendleft(f)
        a = ''.join(list(queue))
        print(a)
        
        answer+=1

    
    return -1