x,y=input().split()
x=int(x)
y=int(y)

suby=y-45

if suby<0:
    suby+=60
    x-=1
    if x<0:
        x+=24
    print(x,suby)

else:
    print(x,suby)
