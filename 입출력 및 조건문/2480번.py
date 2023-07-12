

A,B,C=map(int,input().split())

if A== B==C :
    money=10000+1000*A
    
elif A==B:
    money=1000+100*A
elif A==C:
    money=1000+100*A
elif B==C:
    money=1000+100*B
else:
    money=max(A,B,C)

print(money)