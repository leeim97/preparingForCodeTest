# 6만개니까 시간 복잡도 n
num = int(input())

for n in range(num):
    a, b, N = map(int, input().split())
    sums = 0
    cnt = 0

    while sums <= N:

        if a > b:
            b += a
            sums = b
            cnt += 1
        else:
            a += b
            sums = a
            cnt += 1

    print(cnt)은