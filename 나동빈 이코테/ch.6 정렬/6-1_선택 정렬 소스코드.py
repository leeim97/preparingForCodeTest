array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)-1):
    min_index=i
    print('i:',i)
    for j in range(i+1,len(array)):
        print('j:',j)
        if array[min_index]>array[j]:
            array[min_index] , array[j]=array[j],array[min_index]

print(array)