def solution(quiz):
    
    answer = []
    
    for i in quiz:
        a,ki,b,eq,c=i.split(" ")
        if ki == '+':
            if int(a)+int(b) == int(c):
                answer.append('O')
            else: 
                answer.append('X')
        elif ki == '-':
            if int(a)-int(b) == int(c):
                answer.append('O')
            else: 
                answer.append('X')
        
        
    
    return answer