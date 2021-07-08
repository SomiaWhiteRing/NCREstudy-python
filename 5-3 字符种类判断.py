def Num(a):
    Number=Letter=Space=Other=0
    for i in a:
        if i == " ":Space+=1
        elif ord('0') <= ord(i) and ord('9') >= ord(i):Number+=1
        elif ord('a') <= ord(i) and ord('z') >= ord(i)\
             or ord('A') <= ord(i) and ord('Z') >= ord(i):Letter+=1
        else:Other+=1
    print("共有%d个字母，%d个数字，%d个空格，%d个其他符号。"%(Letter,Number,Space,Other))

UserInput = input("请输入要判断的字符串")
Num(UserInput)
