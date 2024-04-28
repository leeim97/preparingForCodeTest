food_times = list(map(int,input().split()))
k=int(input())


len = len(food_times)

def solution(food_times, k):
    # cnt는 차례를 나타내기위해
    # i는 시간
    i=0
    cnt = 0
    while i==k or sum(food_times) != 0:
        # 차례가 계속 도므로 나머지로 나타냄
        turn = cnt% len
        if food_times[turn] ==0:
            cnt+=1
            continue

        food_times[turn]-=1
        cnt+=1
        i+=1

    # 고장났던 시간에 저장된 food_times로 작동
    answer=-1
    for i in range(cnt%len,len):
        if food_times[i]!=0:
            answer = i
        else:
            continue
    return answer

result=solution(food_times,k)
print(result)