num = int(input())

for k in range(num):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    maxN = 0
    if len(arr1) > len(arr2):
        # 옮겨 다니기
        for i in range(len(arr1) - len(arr2) + 1):
            sumN = 0
            for j in range(len(arr2)):
                sumN += arr1[i + j] * arr2[j]
            if sumN > maxN:
                maxN = sumN


    else:
        # 옮겨 다니기
        for i in range(len(arr2) - len(arr1) + 1):
            sumN = 0
            for j in range(len(arr1)):
                sumN += arr2[i + j] * arr1[j]
            if sumN > maxN:
                maxN = sumN
    print(f'#{k+1} {maxN}')