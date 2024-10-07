def make_sec(time):
    m,s = map(int,time.split(":"))
    sec  = m*60 + s
    
    return sec

def solution(video_len, pos, op_start, op_end, commands):
    v = make_sec(video_len)
    pos  = make_sec(pos)
    start = make_sec(op_start)
    end = make_sec(op_end)
    
    if start <=  pos <= end:
        pos = end
    
    for com in commands:
        if com == 'prev':
            if pos <= 10:
                pos = 0
            elif pos > 10:
                pos -= 10
        elif com == 'next':
            if pos +10 > v:
                pos = v
            elif pos +10 <= v:
                pos +=10
            
        if start <= pos and pos <= end:
            pos = end
            
    time = [pos//60, pos%60]    
    answer = ':'.join(map(lambda x : str(x) if x>=10 else  '0'+str(x) ,time))
    # answer = ':'.join(map(lambda x: str(x) if x>=10 else '0'+str(x), time))
    
    return answer