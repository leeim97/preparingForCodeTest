# 기준이 되는 스코빌 지수 k
# 맵기가 담겨져 있는 배열 scoville
# 내가 잘못 생각한 점: 섞은 음식의 스코빌 지수가 무조건 첫번째 원소보다 크다고 생각했을까?
# 왜 두번째 원소가 k보다 크다고는 생각 못했을까 -> 첫번째 원소 때문에 어쨋든 섞어야됌
# while len(arr) >1  에서 while arr[k]>=0 and len(arr)>1로 하니 해결

import heapq

def solution(scoville, k):
    temp = 0
    cnt = 0
    arr = []
    for i in scoville:
        heapq.heappush(arr,i)
    
    if arr[0] >= k:
        return cnt
    
    while arr[0] < k and len(arr) >1 :
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        temp = first + 2*second
        heapq.heappush(arr,temp)
        
#         temporary = heapq.heappop(arr)
#         heapq.heappush(arr,temporary)
        
        cnt+=1
        # if temporary >= k :
        #     break
        
        
    if  heapq.heappop(arr)< k :
        cnt = -1

    return cnt