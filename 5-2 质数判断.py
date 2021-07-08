def Num(a):
    try:
        for i in range(2,a-1):
            if a%(i+1)==0:
                return False
        return True
    except:
        print("输入的不是整数")
