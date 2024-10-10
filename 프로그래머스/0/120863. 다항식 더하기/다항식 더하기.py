def solution(polynomial):
    
    pnum = []
    num = []
    so = polynomial.split(" ")
    print(so)
    
    for i in so:
        if 'x' in i:
            if i.rstrip('x') == '':
                n=1
            else: 
                n = int(i.rstrip('x'))
            
            pnum.append(n)
        else : 
            if i == '+':
                continue
            print(i)
            num.append(int(i))
                
    if len(pnum) == 0:
        answer=f'{sum(num)}'
    elif len(num) == 0:
        answer = f'{ "" if sum(pnum) ==1 else sum(pnum)}x'
    else:
        answer = f'{"" if sum(pnum) ==1 else sum(pnum)}x + {sum(num)}'
    
    return answer