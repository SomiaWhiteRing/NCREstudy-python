import random
letter = [chr(i) for i in range(ord("a"),(ord("z")+1))] + \
         [chr(i) for i in range(ord("A"),(ord("Z")+1))]
letters = letter + list(range(1,10))
Nums = eval(input("要输出几个数字？"))
for Num in range(Nums):
    for lst in range(8):
        print(letters[random.randint(0,60)] , end="")
    print('\n')
