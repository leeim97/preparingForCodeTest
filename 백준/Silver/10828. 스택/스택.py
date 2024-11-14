import sys
num = int(input())
stack = []
for i in range(num):
    sen = sys.stdin.readline()
    # print(type(sen))
    # print(sen.rstrip())
    # print('asdf')
    sen = sen.rstrip()
    
    if sen[0:4] =='push':
        a,X = sen.split()
        # print(a,X)
        stack.append(X)
    elif sen == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif sen == 'size':
        print(len(stack))
    elif sen == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif sen == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

