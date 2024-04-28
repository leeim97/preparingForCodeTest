# 답 봐버림
num = int(input())

tra = list(map(int,input().split()))

tra.sort()

# result 그룹수
result = 0

# count 인원수
count = 0

for i in tra:
    count+=1
    if count >= i:
        result+=1
        count=0

print(result)

