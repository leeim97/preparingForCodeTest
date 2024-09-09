# from collections import deque

# BFS
def solution(numbers, target):
    answer = 0
    # queue = deque()
    leaves = [0]
    for i in numbers:
        temp = []
        for leaf in leaves:
            temp.append(leaf+i)
            temp.append(leaf-i)
        leaves = temp
        
    for leaf in leaves:
        if leaf == target:
            answer +=1
            
    return answer                                                                                                                                                                                                                                                        