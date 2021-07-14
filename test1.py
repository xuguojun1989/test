
def check():
    dict1={"a":{"aa":11,"bb":[1,2]},"b":2,"c":3}
    dict2={"b":2,"a":1,"c":3}

    print(sorted(dict1))
    print(sorted(dict2))
    print(list(zip(sorted(dict1),sorted(dict2))))
    flag=True
    for list1,list2 in list(zip(sorted(dict1),sorted(dict2))):
        if dict1[list1] != dict2[list2]:
            print(list1,dict1[list1],list2,dict2[list2])
            flag=False

    return flag

print(check())