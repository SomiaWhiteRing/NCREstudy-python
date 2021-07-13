def repeat(set1):
    for test1 in set1:
        set2 = set1.copy()
        set2.remove(test1)
        for test2 in set2:
            if test1 == test2:
                return True

ipt = list(input("请输入一串字符"))
if repeat(ipt):
    print("其中有字符重复")
else:
    print("其中无字符重复")


