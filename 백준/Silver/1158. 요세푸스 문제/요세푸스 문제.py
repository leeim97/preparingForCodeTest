num, cnt = list(map(int,input().split()))

arr = [ i for i in range(1,num+1)]

# 인덱스가 0부터 시작하니까 -1
index = cnt - 1
print('<',end='')
while len(arr)>1:
    # print(arr,len(arr))
    print(f'{arr.pop(index)},',end = ' ')
    index = ((index-1)% len(arr) + cnt ) %  len(arr)

print(f'{arr.pop()}>')

# print(arr.pop(0))
