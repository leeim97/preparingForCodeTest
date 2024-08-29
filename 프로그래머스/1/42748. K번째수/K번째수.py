# 얉은 복사, 깊은 복사

def solution(array, commands):
    answer = []
    
    
    for i in commands:
        first = i[0] -1
        second = i[1] 
        
        temp = array[first:second]
        temp.sort()
        answer.append(temp[i[2]-1])

    return answer