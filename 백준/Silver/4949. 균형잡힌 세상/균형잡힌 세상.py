sen = 'asdf'
while sen :
    sen = input().split('.')[0]
    if len(sen) <=0:
        break
    arr = list(sen)
    stack = []

    for i in arr:
        if i == ')':
            if len(stack) < 1:
                stack.append('(')
                break
            temp = stack.pop()
            if temp != '(':
                stack.append('(')
                break
        elif i == ']':
            if len(stack) < 1:
                stack.append(']')
                break
            temp = stack.pop()
            if temp != '[':
                stack.append('[')
                break
        elif i == '[':
            stack.append(i)
        elif i == '(':
            stack.append(i)

    # print(stack)
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

