h,b,c,s=map(int,input().split())

mem=h*b*c*s/8/1024/1024

print(format(mem,"0.1f"),"MB")