n= int(input(),16)

for i in range(1,16):
    print("%X"%n,"*%X"%i,"=%X"%(n*i),sep="")



# print(f"{n:X} * {i:X} = {n * i:X}")  혹은
# print("%X*%X=%X",%(n,i,n*i))