str="123456abcdef"
list_str=list(str)
print(list_str)
temp=0
for i in range(0,len(list_str)//2):
    list_str[2*i],list_str[2*i+1]=list_str[2*i+1],list_str[2*i]
print(list_str)
print("".join(list_str))

print(list(range(0,10)))

a='hello'
b='world'
a,b=b,a
print(a)
print(b)
