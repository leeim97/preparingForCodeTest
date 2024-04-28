

# N은 볼링공의 개수 M 무게

N,M = map(int,input().split())

ball = list(map(int,input().split()))

# 조합 개수
count=0

for i in range((N)-1):
    for j in range(i+1,(N)):
        if ball[i] == ball[j]:
            continue
        else:
            count+=1
print(count)