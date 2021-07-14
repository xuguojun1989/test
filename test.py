import re
print(int("123"))

try:
    print(int("aaa"))

except:
    print("aaa不能转化")

str="192.168.1.1"
print(str.split("."))

print()
#'^(([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$'

def checkip(str):
    compile_ip=re.compile('^(([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.)((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){2}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$')
    if compile_ip.match(str):
        return True
    else:
        return False

print(checkip("1929.168.0.0"))

def checkip1(str):
    flag=True
    if '.' not in str:
        flag=False
    list=str.split('.')

    if len(list) != 4:
        flag=False
    i=0
    for list_num in list:
        if i==0:
            if int(list_num) >= 1 and int(list_num) <= 255:
                pass
            else:
                flag=False
        else:
            if int(list_num) >= 0 and int(list_num) <= 255:
                pass
            else:
                flag=False
        i=i+1

    return flag

print(checkip1("192"))

def checkip2(str):

    try:
        flag=True
        list=str.split('.')
        if len(list) != 4:
            flag=False
        elif int(list[0])>= 1 and int(list[0]) <= 255 and int(list[1])>= 0 and int(list[1]) <= 255 and int(list[2])>= 0 and int(list[2]) <= 255 and int(list[3]) >= 0 and int(list[3]) <= 255:
            pass
        else:
            flag=False
    except:
        flag=False

    return flag

print(checkip2("19211ww"))

def test(num):
    flag=True
    try:
        if int(num)%4 == 0 and int(num)%100 != 0:
            pass
        elif int(num)%400 == 0:
            pass
        else:
            flag=False
    except:
        flag=False

    return flag

print(test(1900))








