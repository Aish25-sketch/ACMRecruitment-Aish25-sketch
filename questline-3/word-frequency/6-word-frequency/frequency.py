def frequency(file):
    count={}
    f=open(file,"r")
    words=f.read().lower().split()
    f.close()

    for w in words:
        if w in count:
            count[w]=count[w]+1
        else:
            count[w]=1
    return count
count=frequency("input.txt")
f=open("output.txt","w")
for w in count:
    f.write(w+"-->"+str(count[w])+"\n")
f.close()
