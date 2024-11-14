for i in range(10):
    num = int(input())
    arr = list(map(int, input().split()))
    answer = 0

    for j in range(2, len(arr) - 2):
        temp = []
        temp.append(arr[j] - arr[j - 2])
        temp.append(arr[j] - arr[j - 1])
        temp.append(arr[j] - arr[j + 1])
        temp.append(arr[j] - arr[j + 2])

        if min(temp) < 0:
            continue
        else:
            answer += min(temp)

    print(f'#{i+1} {answer}')
