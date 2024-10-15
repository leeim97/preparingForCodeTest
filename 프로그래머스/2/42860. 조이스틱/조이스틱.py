def solution(name):
    spell_move= 0
    sea = len(name) -1
    
    for i,char in enumerate(name):
        spell_move += min( ord(char)-ord('A'),  ord('Z')-ord(char)+1  )
        
        cnt= i+1
        while cnt < len(name) and name[cnt] == 'A':
            cnt+=1
        
        sea = min([sea, 2*i + len(name)-cnt, i + 2*(len(name)-cnt) ])
        
    
    return sea + spell_move