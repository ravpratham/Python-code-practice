f = open(r"C:\Users\ravpr\Downloads\Teachers Day.txt","r")
fh = f.read()
words = fh.split()
count = 0
for i in words:
    if i in fh:
        count+=1
print(count)