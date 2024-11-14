num = int(input())
arr = list(map(int,input().split()))
print(num,arr)

answer = 0
visit = [False]*9

def bfs(num, arr, cnt):
    global answer,visit
    answer = max(answer,cnt)

    for i,idx in enumerate(arr):
        visit[i] = True
        bfs(num,arr,cnt)
        visit[i] = False