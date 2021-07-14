def jump(n):
    if n==1 or n==2:
        return n
    print(n)
    return jump(n-1)+jump(n-2)

print(jump(5))

# jump(2)+jump(3)
# 2+jump(2)+jump(1)
# 2+2+1
# jump(4)+jump(3)
# jump(2)+jump(3)+jump(1)+jump(2)
# 2+jump(2)+jump(1)+jump(2)+1+2
# 2+2+1+2+1+2

