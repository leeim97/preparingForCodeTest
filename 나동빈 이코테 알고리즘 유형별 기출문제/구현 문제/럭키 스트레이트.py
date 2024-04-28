

# 럭키 스트레이트 조건 자리수 기준 반반 나눠서 합이 같을때, 자리수는 무조건 짝수로만 주어진다
# 점수 값 입력
score = int(input())

# 자릿수 그냥 최소 자릿수가 2이므로
digit=2

# 앞부분과 뒷부분
forward=0
back=0

# 자릿수 세기
temp=score
cnt=0
while temp>0:
    temp=temp//10
    cnt+=1

# 앞 뒤 각각 더하기
i=1
while i<=cnt:
    if i <=cnt/2:
        back += score%10

    elif i>cnt/2:
        forward += score%10
    i+=1
    score = score//10

if back == forward:
    print("LUCKY")
else:
    print("READY")



