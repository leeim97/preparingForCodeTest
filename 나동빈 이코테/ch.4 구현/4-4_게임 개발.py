def turn_left():
    global dir
    dir = (dir-1)%4



n,m= map(int,input().split())

x,y,dir= map(int,input().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

count=1
dir_cnt=0
while True:
    turn_left()
    vx=x+ dx[dir]
    vy=y+ dy[dir]

    if arr[vx][vy] == 1:  #바라본 방향이 바다인경우
        dir_cnt+=1
        continue
    elif arr[vx][vy] == 0:  #바라본 방향이 육지인 경우
        x=vx
        y=vy
        arr[x][y]=1
        count+=1

    if dir_cnt==4:
        mx=x-dx[dir]
        my=y-dy[dir]
        if arr[mx][my]==1:
            break
        else:
            x=mx
            y=my


print(count)
