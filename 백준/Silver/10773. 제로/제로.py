import sys

num = int(input())
stack = []

for _ in range(num):
    n = int(sys.stdin.readline())
    if n == 0 :
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))