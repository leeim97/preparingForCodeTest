x,y=input().split()
z=input()
x=int(x)
y=int(y)
z=int(z)

if y+z>=60:
    p=(y+z)//60
    y=(y+z)%60
    x+=p
    x%=24
    print(x,y)

else:
    print(x,y+z)
