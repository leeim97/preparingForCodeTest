import sys
num = int(input())

fir = list(input())
fir.sort()
#전체 맞은갯수
cnt=0
for i in range(1,num):
    fi = fir.copy()
    # 한 구간 틀린갯수
    c=0

    arr= list(sys.stdin.readline().rstrip())

    # 단어길이 2개이상 차이나면 끝
    if abs(len(fir) - len(arr)) >=2:
        continue


    for j in arr:
        start = 0
        end = len(fi) - 1
        find = False
        while start<=end:
            mid = (start+end)//2

            if fi[mid] == j:
                find=True
                fi.pop(mid)
                break
            elif fi[mid] > j:
                end = mid-1
            elif fi[mid] < j:
                start = mid +1

        if find == False:
            c+=1

        if c >1:
            break

    if c<=1:
        cnt+=1

print(cnt)