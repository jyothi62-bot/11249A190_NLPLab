text="I like NLP. I like Python."
w=text.split()
print("word frequency :")
for i in w:
    if w.count(i)>0:
        print(i,":",w.count(i))
        while i in w:
            w.remove(i)
    w = text.split()
    done=[]
for i in range(len(w)):
    print((w[i]))
for i in range(len(w)-1):
    print((w[i],w[i+1]))
