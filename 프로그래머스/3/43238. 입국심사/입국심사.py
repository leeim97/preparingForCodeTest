def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times)*n
    
    while left <= right:
        mid = (left+right) // 2
        
        # 계속 mid를 바꾸며 검사를 하기때문에 people를 계속 0으로 초기화
        people=0
        
        for time in times: 
            people += mid // time
            
            if people >= n :
                break
            
        if people >= n:
            right = mid - 1
            # 몇분이 걸렸는지
            answer = mid
            
        elif people < n :
            left = mid +1
            
    
    return answer