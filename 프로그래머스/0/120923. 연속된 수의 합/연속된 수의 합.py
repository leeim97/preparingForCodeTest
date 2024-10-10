def solution(num, total):
    # 등차수열로 풀자
    # total = start + start+1 + start+2 + start+3 + ''' + start + num-1
    # total = start*num + (1+2+'''+num-2 + num-1)
    
    start = (total - sum(range(num))) / num
    
    answer = [start+i for i in range(0,num)]
    
    
    return answer