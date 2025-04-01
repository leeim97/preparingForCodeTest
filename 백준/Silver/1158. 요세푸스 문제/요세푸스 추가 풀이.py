from collections import deque
num, cnt = list(map(int,input().split()))

arr = deque([ i for i in range(1,num+1)])
ans = []

while arr:
    for _ in range(cnt-1):
        arr.append(arr.popleft())

    ans.append(str(arr.popleft()))

print(f'<{", ".join(ans)}>')
# print(arr.pop(0))