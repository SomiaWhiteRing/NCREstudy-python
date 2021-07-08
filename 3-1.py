a = input("请输入一个大于100的整数")
if a.isdigit() :
    if (type(eval(a)) == type(1)) & (eval(a) >= 100) :
        print(eval(a)//100)
    else :
        print("输入的不是大于一百的整数")
else :
    print("输入的不是大于一百的整数")
