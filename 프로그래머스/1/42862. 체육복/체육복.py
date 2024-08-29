# 처음에는 양옆으로 생각했는데 굳이그러지않고 바로 다음만 생각했음
# 2 0 1 
# 1 0 2 이라면?
# 1 2 0 1 을 생각못함
# 질문을 제대로 이해 못함 도난도 당할수있고 동시에 여벌옷도 있을수있다

def solution(n, lost, reserve):
    # 맨앞은 -1으로 그냥 제외 그 다음부터 1번 2번 ...
    arr = [1] * (n+1)
    arr[0] = -1
    for i in reserve:
        arr[i] += 1 
    for i in lost:
        arr[i] -= 1
    print(arr)

    for i in range(1,n+1):
        if arr[i] == 0:  # 체육복이 없는 경우
            if i > 1 and arr[i - 1] == 2:  # 이전 학생이 여분이 있는 경우
                arr[i] += 1
                arr[i - 1] -= 1
            elif i < n and arr[i + 1] == 2:  # 다음 학생이 여분이 있는 경우
                arr[i] += 1
                arr[i + 1] -= 1

        else:
            continue
    cnt = 0
    for i in arr:
        if i == 1 or i==2:
            cnt+=1
    print(arr)
    return cnt