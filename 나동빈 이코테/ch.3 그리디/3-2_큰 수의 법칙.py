N,M,K=map(int,input().split())  #N은 배열 크기 M은 더하는 횟수 K는 같은 수를 더할때 최대 중복 횟수
data=list(map(int,input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

cnt= M //(K+1)*K
cnt += M % (K+1)

total= cnt*first + (M-cnt)*second


print(total)