def solution(N, number):
    
    arr = [set() for _ in range(9)] # 맨앞은 무시하고 s[1],s[2]...s[8]
    for i in range(1,9):
        arr[i].add(int(str(N)*i))
    
    for i in range(1,9):
        for j in range(1,i):
            for a in arr[j]:
                for b in arr[i-j]:
                    arr[i].add(a+b)
                    arr[i].add(a-b)
                    arr[i].add(a*b)
                    if b != 0:
                        arr[i].add(a//b)
        if number in arr[i]:
            return i
    
    
    return -1