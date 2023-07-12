score=input()
score=int(score)

if 90<=score and score<=100:
    print('A')
elif 80<=score and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
else:
    print('F')