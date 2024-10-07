def solution(babbling):
    ma = ["aya", "ye", "woo", "ma"]
    answer = 0 
    
    for ba in babbling:
        result =0
        for j in ma:
            if ba.find(j) != -1:
                result += len(j)
        if result == len(ba):
            answer+=1
    
    return answer