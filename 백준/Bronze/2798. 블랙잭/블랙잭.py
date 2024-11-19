num, s = map(int, input().split())

arr = list(map(int,input().split()))
ans = 0

for a in arr:
    for b in arr:
        for c in arr:
            if a==b or b==c or a==c:
                continue
            else:
                temp = a + b + c
                if (temp <= s) and temp > ans:
                    ans = temp
                    # print(a, b, c)/
print(ans)