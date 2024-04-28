s = input()

# 이진법에서 0의 갯수와 1의 갯수를 새기 위해서
cnt0 = 0
cnt1 = 0

# 더 적은 숫자를 뒤집기위해 수량 체크
for i in s:
    if i =='0':
        cnt0+=1
    elif i == '1':
        cnt1+=1

# 0이 더 적은경우 0을 바꿔줘야지
if cnt0<cnt1:
    result0=0
    for i in range(len(s)-1):
        if s[i]=='0':
            # 연속된 0이 아닌 다음이 1로 끊기는 경우
            if s[i+1]=='1':
                result0+=1

    #마지막 숫자가 0인경우도 바꿔줘야하니 카운트
    if s[len(s)-1] == '0':
        result0+=1
    print(result0)



# 1이 더 적은경우 0을 바꿔줘야지
else:
    result1 = 0
    for i in range(len(s) - 1):
        if s[i] == '0':
            # 연속된 0이 아닌 다음이 1로 끊기는 경우
            if s[i + 1] == '1':
                result1 += 1

    # 마지막 숫자가 0인경우도 바꿔줘야하니 카운트
    if s[len(s) - 1] == '1':
        result1 += 1
    print(result1)