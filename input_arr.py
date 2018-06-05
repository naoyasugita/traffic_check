def test(num):
    f = open("signalvalue"+str(num)+".txt","r")
    words = f.read()
    word = words.split()
    print(word)
    f.close()
