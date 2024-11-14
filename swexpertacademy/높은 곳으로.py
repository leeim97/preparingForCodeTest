print()

num = int(input())

for _ in range(num):
    n, p = map(int, input().split())


    sumN = ((n + 1) * n) / 2
    if sumN < p:
        print(int(sumN))
    else:
        cnt = 0
        sumS = 0
        while cnt <= n :
            if sumS == p:
                sumS-=cnt

            cnt += 1
            sumS+=cnt



        print(sumS - cnt-1)



