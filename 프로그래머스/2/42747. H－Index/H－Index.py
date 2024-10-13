def solution(citations):
    
    citations.sort()
    maxM = 0
    
    for i in range(max(citations),1,-1):
        cntM = 0
        cntm = 0
        for j in citations:
            if j>=i:
                cntM+=1
            if j <= i :
                cntm +=1
        if cntM >= i and cntm <=i:
            maxM = i
            break
    
    answer = maxM
    return answer