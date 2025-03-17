num = int(input())

dp = [0]*(num+1)

if num >=2:
    dp[2] = 1
if num >=3:
    dp[3] = 1

if num>=4:
    for i in range(4,num+1):
        dp[i] = dp[i-1]+1
        if i % 3 == 0:
            dp[i] = min(dp[i//3]+1,dp[i]) 
        if i %2 ==0:
            dp[i] = min(dp[i//2]+1,dp[i]) 



# for i in range(num+1):
#     print(i,dp[i])
print(dp[num])