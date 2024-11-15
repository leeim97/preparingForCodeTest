import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

# print(N,A)
# print(M,arr)


for i in arr:
    start = 0
    end = N-1
    ex = False

    while start <=end:
        mid = (start + end)//2


        if A[mid] == i:
            print('1')
            ex = True
            break
        elif A[mid] > i:
            end = mid - 1
        elif A[mid] < i :
            start = mid + 1

    if not ex:
        print('0')

        