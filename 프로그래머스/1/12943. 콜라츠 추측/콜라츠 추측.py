def solution(num):
    answer = 0
    for i in range(500):
        if i==0 and num==1:
            return 0
        if num ==1:
            return answer
        
        if num%2==0:
            num/=2
        else:
            num=num*3+1
        answer+=1
    answer = -1
    
    return answer