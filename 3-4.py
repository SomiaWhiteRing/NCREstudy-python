text = input("请输入一个数字")
answer = ""
for i in text:
    answer = i + answer
if answer == text:
    print("这个数字是回文数")
else:
    print("这个数字不是回文数")
