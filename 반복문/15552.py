import sys

num=int(sys.stdin.readline().rstrip())

for i in range(num):
    A,B=map(int,sys.stdin.readline().split())
    print(A+B)
