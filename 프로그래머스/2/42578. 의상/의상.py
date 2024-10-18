from itertools import combinations
def solution(clothes):
    arr = {}
    answer = 1
    
    for wear,kind in clothes:
        if kind in arr.keys():
            arr[kind] += [wear]
        else:
            arr[kind] = [wear]
    
    for a,b in arr.items():
        answer *= (len(b)+1)
        
    print(arr) 
    return answer -1