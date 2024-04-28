# # 풀면서 느낀점
# money에서 두개의 항목을 더한개아닌 여러개의 항목을 더하는 과정을 생각하지 못했다

# 동전 개수
num = int(input())

# 동전 종류
money = list(map(int,input().split()))
money.sort()


target = 1

for x in money:
    if target < x:
        break
    target += x

print(target)