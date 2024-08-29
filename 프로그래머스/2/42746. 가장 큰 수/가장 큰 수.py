# 10이상의 수는 그대로 들어간다~

def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x : x*3 , reverse = True)
    answer = ''.join(numbers)
    
    
    return str(int(answer))