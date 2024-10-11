def solution(participant, completion):
    
    hashDict = {}
    sumhash=0
    
    for i in participant:
        hashDict[hash(i)] = i
        sumhash += hash(i)
        
    for j in completion:
        sumhash -= hash(j)
    
    print(hashDict[sumhash])
    
    
    return hashDict[sumhash]