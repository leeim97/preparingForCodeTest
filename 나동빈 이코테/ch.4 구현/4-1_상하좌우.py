N= int(input())

x=1
y=1

dirs=list(input().split())

for dir in dirs:
    if dir == 'L':
        if y==1:
            continue
        else:
            y-=1


    elif dir == 'R':
        if y==N:
            continue
        else:
            y+=1

    elif dir == 'U':
        if x==1:
            continue
        else:
            x-=1

    elif dir == 'D':
        if x== N:
            continue
        else:
            x+=1


print(x,y)