def solution(score):
    asdf= []
    answer = []
    for sc in score:
        asdf.append((sc[0]+sc[1])/2)
    
    ss=sorted(asdf,reverse = True)
    print(asdf)
    print(ss)
    
    
    for sc in asdf:
        for i, sd in enumerate(ss):
            if sc==sd:
                answer.append(i+1)
                break
    
    return answer