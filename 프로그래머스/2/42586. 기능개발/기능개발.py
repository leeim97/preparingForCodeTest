from collections import deque

def solution(progresses, speeds):
    answer = []
    
    queue =deque(progresses)
    spee = deque(speeds)
    # day가 기가막히네ㅐ
    cnt=0
    day=0
    while queue:
        if (queue[0] + day*spee[0]) >= 100:
            queue.popleft()
            spee.popleft()
            cnt+=1
        else:
            if cnt>0:
                answer.append(cnt)
                cnt=0
            else:
                day+=1
        
        
        
    answer.append(cnt)
    return answer