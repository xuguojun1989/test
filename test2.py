# a=input()
# print(a)

list_words = ["apple",'banana','grape','apple','dog','class','dog','dog']
dict_words = {}
for word in list_words:
    if None == dict_words.get(word, None):
        dict_words[word] = 1
    else:
        dict_words[word] = dict_words[word] + 1

print(dict_words)

list_wordss=[[v[1],v[0]] for v in dict_words.items()]
print(list_wordss)
list_wordss.sort(reverse=True)
print("list_wordss")
print(list_wordss)

new_dic3 = sorted(dict_words.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
print('new_dic3')
print(new_dic3)

#new_dict = sorted(dict_words.values())
print('xu sort')
#返回重新排序的列表
print(sorted(dict_words.items(), key=lambda item:item[1]))
#print(new_dict)

dicttest_words={"apple":2,"pear":3,"summer":4}
dicttest_words["popur"]=5
print(dicttest_words)
print(dicttest_words.items())
for test_word in dicttest_words.items():
    print(test_word)


list_test=[1,2,3]
list_test[0]=0
#list_test[3]=4
print(list_test)

'''
print(len(list))
listsum=[]
j=0

flag=True
act=len(list)
for i in range(0, len(list)-1):
    print(i)
    sum = 1
    for j in range(i+1,len(list)-1):
        if list[i]==list[j]:
            sum=sum+1
            print(list[j])
            print(sum)
            list.remove(list[j])
            act=act-1
            print(list)
        j=j+1
    print("添加list")
    if flag==True and i < act:
        listsum.append(list[i])
        print("添加sum")
        listsum.append(sum)
        flag==False
    i=i+1
    flag == True

print(listsum)
'''