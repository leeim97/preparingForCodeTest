
def solution(number, k):
    le = k
    stack =[]
    
    for i in number:
        while stack and stack[-1] < i and k>0 :
            
            stack.pop()
            k-=1
        stack.append(i)
    
    answer = ''.join(stack)
    
    
    
    return  ''.join(answer[:len(answer) - k])