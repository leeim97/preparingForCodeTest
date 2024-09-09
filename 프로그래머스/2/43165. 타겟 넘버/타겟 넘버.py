from collections import deque

# BFS
def solution(numbers, target):
    answer = 0
    leaves = deque([0])
    
    for i in numbers:
        temp = []
        while leaves:
            leaf = leaves.popleft()
            temp.append(leaf+i)
            temp.append(leaf-i)
        leaves = deque(temp)
        
    for leaf in leaves:
        if leaf == target:
            answer +=1
            
    return answer                                                                                                                                                                                                                                                        