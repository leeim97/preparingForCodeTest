def solution(price, money, count):
    answer=0
    for i in range(1,count+1):
        answer+=price*i
        print(answer)
    num = answer- money
    print(num,answer)
    
    if num<0:
        return 0
    else:
        return num
    
    return num