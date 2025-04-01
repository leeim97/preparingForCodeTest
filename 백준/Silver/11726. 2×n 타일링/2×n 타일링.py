n = int(input())

dp = [0]*1001
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)

# 4 -> 3(2(1,1),1),1  2,2
# 5 -> 3,2  4,1

