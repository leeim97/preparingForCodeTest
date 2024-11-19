# 보텀 업 방식
# 가짓수 3으로 만 만들수 있는거, 5로만 만들수있는거, 3과5로만 만들수 있는거, -1
# 차근차근 아래부터 데이터를 쌓기

we = int(input())


sugar = [-1]*5001

sugar[3]=1
sugar[5]=1

for i in range(6,we+1):
    if i %5 ==0:
        sugar[i] = sugar[i-5]+1
    elif i%3 ==0:
        sugar[i] = sugar[i-3]+1
    elif sugar[i-3] >0 and sugar[i-5]>0:
        sugar[i] = 1 + min(sugar[i-3],sugar[i-5])

print(sugar[we])