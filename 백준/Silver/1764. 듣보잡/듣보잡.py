import sys

N, M = map(int,input().split())

arr1 = []
arr2 = []
for i in range(N):
    name = sys.stdin.readline().rstrip()
    arr1.append(name)

for j in range(M):
    name = sys.stdin.readline().rstrip()
    arr2.append(name)
arr1.sort()
arr2.sort()

ans = (set(arr1) & set(arr2))
print(len(ans))

a = list(ans)
a.sort()

for i in a:
    print(i)
