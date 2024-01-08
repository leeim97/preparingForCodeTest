ch= input()
a="a"

while True:
    if a== chr(ord(ch)+1):
        break
    print(a,end=" ")
    a=chr(ord(a)+1)

