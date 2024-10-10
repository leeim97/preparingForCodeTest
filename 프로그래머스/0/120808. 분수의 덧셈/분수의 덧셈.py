def solution(numer1, denom1, numer2, denom2):
    numer = numer1*denom2 +  numer2* denom1
    denom = denom1*denom2
    
    i_min = min(numer,denom)
    
    for i in range(i_min,1,-1):
        if denom%i == 0 and numer%i==0:
            denom/=i
            numer/=i
            break
    
    answer = [numer, denom]
    return answer