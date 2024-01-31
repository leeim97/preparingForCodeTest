pos= input()

x=int(ord(pos[0]))-int(ord('a'))+1
y=int(pos[1])

steps=[[-2,-1],[-2,1],[-1,2],[1,2],[2,-1],[2,1],[-1,-2],[1,-2]]

cnt=0
for step in steps:
    if x+step[0]<1 or x+step[0]>8 or y+step[1]<1 or y+step[1]>8:
        continue
    else:
        cnt+=1

print(cnt)