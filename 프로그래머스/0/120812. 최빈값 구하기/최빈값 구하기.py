def solution(array):
    answer=0
    cnt = 0
    ar=[]
    max_c=0
    for i in array:
        cnt= 0
        for j in array:
            if i==j:
                cnt+=1
        if max_c < cnt:
            max_c = cnt
            
    for i in array:
        if array.count(i) == max_c:
            ar.append(i)
            
    if len(set(ar)) == 1:
        answer = ar[0]
    else:
        answer = -1
        
    
    return answer