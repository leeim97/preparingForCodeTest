ans = []
for i in range(1,10001):
    # print(i)
    temp = i
    num=0
    num+= temp

    while temp>0:
        num+= temp%10
        temp= temp//10


    ans.append(num)
    ans.sort()

e= [i for i in range(1,10001)]

an = set(e) - set(ans)
a = list(an)
a.sort()
for j in a:
    print(j)