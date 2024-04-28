str = input()

# 연산의 결과 값
result = 0
# 처음 숫자 대입하기 위해 cnt 왜냐면 처음 result 값을 0으로 설정했을때 다음 값을 계속 곱해도 0이기때문에
cnt=0
for i in str:

    num = int(i)

    if cnt == 0 :
        result=num
        cnt+=1
        continue

    if num == 0:
        result+=num
    else:
        if result ==0:
            result+=num
        else:
            result*=num

print(result)


