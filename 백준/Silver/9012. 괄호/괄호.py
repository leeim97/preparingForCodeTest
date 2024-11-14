num = int(input())

for i in range(num):
    # print(i+1)
    arr = list(input())
    stack = []

    for i in arr:
        if i == ')':
            if len(stack) <=0:
                stack.append(')')

                break
            stack.pop()
        elif i == '(':
            stack.append('(')


    if len(stack) == 0 :
        print('YES')
    else:
        print('NO')