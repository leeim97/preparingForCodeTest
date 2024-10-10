def solution(numlist, n):
    
    for i in range(len(numlist)):
        numlist[i] -= n 
    
    for i in range(len(numlist)-1):
        for j in range(i+1,len(numlist)):
            if abs(numlist[i]) == abs(numlist[j]):
                if numlist[i] < numlist[j]:
                    temp = numlist[i]
                    numlist[i] = numlist[j]
                    numlist[j] = temp
            else:
                if abs(numlist[i]) > abs(numlist[j]):
                    temp = numlist[i]
                    numlist[i] = numlist[j]
                    numlist[j] = temp
    
    for i in range(len(numlist)):
        numlist[i] += n
            
    return numlist