def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    
    for num,ans in enumerate(answers):
        if one[num%len(one)]== ans:
            cnt[0]+=1
        if two[num%len(two)]== ans:
            cnt[1]+=1
        if three[num%len(three)]== ans:
            cnt[2]+=1
    
    index = []
    ma = max(cnt)
    
    for i,num in enumerate(cnt):
        if ma == num:
            index.append(i+1)

    
    return index