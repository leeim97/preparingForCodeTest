len,wid = map(int,input().split())

d=[[0]*wid for _ in range(len)]

num_bar= int(input())


for _ in range(num_bar):
    bar_len,bar_dir,pos_x,pos_y = map(int,input().split())
    if bar_dir==0:#가로
        for i in range(bar_len):
            d[pos_x-1][pos_y-1+i]=1

    elif bar_dir==1:#세로
        for j in range(bar_len):
            d[pos_x - 1 +j][pos_y -1 ] = 1

for i in range(len):
    for j in range(wid):
        print(d[i][j],end=" ")
    print()

