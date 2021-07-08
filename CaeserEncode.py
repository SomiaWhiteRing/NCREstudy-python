ptxt = input("请输入明文文本")
ntxt = ""
for p in ptxt :
    if 'a' <= p <= 'z' :
        ntxt += chr(ord('a')+(ord(p)-ord('a')+3)%26)
    elif 'A' <= p <= 'Z' :
        ntxt += chr(ord('A')+(ord(p)-ord('A')+3)%26)
    else :
        ntxt += p
print(ntxt)
