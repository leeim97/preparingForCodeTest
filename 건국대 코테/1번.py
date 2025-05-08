word = ["can","bat","bin","son","ear"]
n = int(input())

# print(word[0][1])

result = []
for i in range(len(word)):
    m = i
    for j in range(i+1,len(word)):
        if word[m][n-1] > word[j][n-1]:
                m=j
        elif word[m][n-1] == word[j][n-1]:
            if word[i][n % 3] > word[j][n % 3]:
                m = j

    temp = word[i]
    word[i]=word[m]
    word[m]= temp


print(word)
