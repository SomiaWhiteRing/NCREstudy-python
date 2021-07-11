text = input("请输入需要检测的文本")
text = text.lower()
sheet = dict()
logs = list(range(0,ord('龥')))
for i in logs:
    sheet.update({chr(i):text.count(chr(i))})
while sheet!={}:
    b=c=d=0
    for i in logs:
        b = sheet.get(chr(i),0)
        if b>=d:
            c,d=i,b
    else:
        sheet.pop(chr(c))
        if d != 0:
            print("%s出现了%d次" %(chr(c),d))
        logs.remove(c)
