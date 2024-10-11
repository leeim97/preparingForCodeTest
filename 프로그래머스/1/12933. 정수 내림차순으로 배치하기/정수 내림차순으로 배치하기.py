def solution(n):
    
    answer = list(map(int,list(str(n))))
    answer.sort(reverse = True)
    ans = ''
    for i in answer:
        ans += str(i)
    
    
    return int(ans)