a,b,c = map(int,input().split())
mem= a*b*c/8/1024/1024

print(format(mem,"0.2f"),"MB")