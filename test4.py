list_num=[1,2,3,1,5,6]
tuple_index=(0,0)
list_sum=[]

for i in range(0,len(list_num)):
    for j in range(i,len(list_num)):
        if list_num[i]+list_num[j]==3:
            tuple_index=(i,j)
            list_sum.append(tuple_index)

print(list_sum)

print(str([m+n for m in 'ABC' for n in '123']))





list_test=range(3,len(list_num))
print(list(list_test))

