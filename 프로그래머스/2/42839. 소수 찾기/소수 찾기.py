from itertools import permutations

def sos(num):
    if num <=1:
        print('FALSE')
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num% i ==0:
            print(num)
            return False
        
    return True
    

def solution(numbers):
    sosu = []
    answer = 0
    num = 0
    
    arr = list(numbers)
    
    for i in range(1,len(arr)+1):
        for j in permutations(arr,i):
            sosu.append(int(''.join(list(j))))
            
    for i in list(set(sosu)):
        if sos(i):
            answer+=1
    print(list(set(sosu)))
    
    return answer