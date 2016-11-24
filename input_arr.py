def test(num):
    f = open("signalvalue"+str(num)+".txt","r")
    words = f.read()
    word = words.split()
    print(word)
    f.close()

for i in range(1,1001):
    test(i)
