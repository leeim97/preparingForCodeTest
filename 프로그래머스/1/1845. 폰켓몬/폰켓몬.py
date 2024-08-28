def solution(nums):
    answer = 0
    le = []
    for i in nums:
        if len(le) < len(nums)/2:
            if i not in le:
                le.append(i)
    
    se = set(le)
    return len(se)

