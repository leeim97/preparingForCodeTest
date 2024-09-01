def solution(triangle):
    answer = 0
    
    floor = len(triangle) -1 # 층의 인덱스
    
    
    while floor > 0 :
        
        for i in range(len(triangle[floor])-1): # 각 층 인덱스 0부터 끝가지
            triangle[floor-1][i] += max(triangle[floor][i],triangle[floor][i+1])
        
        floor -= 1
    
    return triangle[0][0]