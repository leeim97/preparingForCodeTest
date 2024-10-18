from collections import deque
def solution(priorities, location):
    
    queue = deque([ (i,p) for i,p in enumerate(priorities)])
    answer = 0
    cnt =0
    while queue:
        temp = queue.popleft()
        if any( temp[1] <i[1] for i in queue ) : 
            queue.append(temp)
        else:
            cnt+=1
            if temp[0] == location:
                answer = cnt
                break
        
    
    
    return answer