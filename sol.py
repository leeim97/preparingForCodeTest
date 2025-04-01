# f(0) =1 0, f(1)=0 1 , f(2) = 1 1, f(3) = 1 2, f(4) = 2 3

dp = [[0,0] for _ in range(41)]

dp[0] = [1,0]
dp[1] = [0,1]


n = int(input())

for _ in range(n):
    num = int(input())

    for i in range(2,num+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]


    print(dp[num][0],dp[num][1])