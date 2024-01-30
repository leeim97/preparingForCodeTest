maze=[[0]*10 for _ in range(10)]
cor=[[0]*10 for _ in range(10)]
for i in range(10):
    maze[i]=list(map(int, input().split()))

cor=maze

cnt=1
for i in range(1,9):
    for j in range(cnt,9):
        if i>=10:
            break

        if maze[i][cnt+1]==1: #부딪힐때
            cor[i][cnt]=9
            i+=1
            print("1")


        elif i==8 and cnt==8:
            cor[i][cnt]=9
            break
            print("2")


        elif maze[i][cnt]==2: #먹이를 만났을때
            cor[i][cnt]=9
            print("3")
            break

        else:
            cnt=j
            cor[i][cnt]=9


            print("4")


for i in range(10):
    for j in range(10):
        print(cor[i][j],end=" ")
    print("")