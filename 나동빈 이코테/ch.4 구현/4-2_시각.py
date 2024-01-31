N= int(input())

h=0
m=0
s=0
cnt=0

while True:
    s+=1
    if s==60:
        s=0
        m+=1
        if m==60:
            m=0
            h+=1

    if h==N and m==59 and s==59:
        break

    if s%10 ==3 or s//10%10==3 or m%10 ==3 or m//10%10==3 or h%10 ==3 or h//10%10==3:
        cnt+=1



print(cnt)