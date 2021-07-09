def Prime200():
    for i in range(2,200):
        for a in range(2,i-1):
            if i%a==0:
                break
        else:
            print(i,end=" ")
Prime200()
