import random
target,guess = random.randint(1,999),0
while guess!=target:
    try:
        guess = eval(input("请猜一个大于0小于1000的整数："))
    except:
        print("你输入的不是数字！")
        continue
    else:
        if guess > 0 and guess < 1000:
            if guess > target:print("猜大了，再试一次吧！")
            if guess < target:print("猜小了，再试一次吧！")
        else:
            print("你输入的数字不在范围内！")
print("恭喜你，猜中啦！")
        
