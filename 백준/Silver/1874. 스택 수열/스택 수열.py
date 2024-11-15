import sys


num = int(input())
top=1
stack = []
op = []
find= True

for _ in range(num):
    n = int(sys.stdin.readline().rstrip())

    while top <= n:
        stack.append(top)
        op.append('+')
        top+=1

    if stack[-1] == n:
        stack.pop()
        op.append('-')
    else:
        # break를 안넣어서 틀림
        find = False


if not find:
    print('NO')
else:
    for i in op:
        print(i)
