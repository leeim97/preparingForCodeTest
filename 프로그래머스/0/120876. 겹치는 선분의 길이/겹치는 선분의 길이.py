from itertools import combinations


def solution(lines):
    answer = 0
    
    count = [0 for _ in range(200)]
    
    for i in lines:
        for j in range(i[0],i[1]):
            count[j+100]+=1
    
    answer += count.count(2)
    answer += count.count(3)
    
    return answer