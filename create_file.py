def mkfile(num):
    for i in range(1,num):
        f = open("signalvalue"+ str(i) + ".txt","w")
        f.write("11 "+ str(11*i) + " 11 " +str(11+i)  +" 11")
mkfile(1000)

