# join 함수를 썻으면 좋았을텐데 join 함수를 까먹었다.


# 문자열 입력
temp = input()

texts = list(temp)
texts.sort()

cnt=0
te=[]

for text in texts:
    if text >= '0' and text <= '9':
        cnt+=int(text)
    else:
        print(text,end='')
print(cnt)



