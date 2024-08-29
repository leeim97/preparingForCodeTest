def solution(sizes):
    answer = 0
    arr = [sorted(i,reverse=True) for i in sizes]
    
    
    w = 0
    h = 0 
    for i in arr:
        if w < i[0]:
            w= i[0]
        if h < i[1]:
            h= i[1]
    print(arr)
    print(w,h)
    answer = w*h
    return answer