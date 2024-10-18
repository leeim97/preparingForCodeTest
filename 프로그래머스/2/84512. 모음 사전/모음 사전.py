def solution(word):
    # 글자수
    cnt = 0
    answer = 0
    ae = ['A','E','I','O','U']
    idx = -1
    
    def dfs(cnt, s):
        nonlocal answer,idx
        if cnt <=5:
            idx+=1
            print(idx, s)
            if s == word:
                answer = idx
        else:
            return
        
        for i in ae:
            dfs(cnt+1,s+i)
            
    
    dfs(0,'')
    
    return answer