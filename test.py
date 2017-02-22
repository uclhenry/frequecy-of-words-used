#
f=open("short.txt","r")
#f.readline()
data = []
for line in f:
    dec =  line.decode("gbk",'ignore')
    data.append(dec)
i=0 
j=0 
words = []  
f.close()
for line in data:
    line=line.strip()
    parts  = line.split(' ')
    for part in parts:
        j+=1
        print j,part
        if part!='\n'  :            
            words.append(part) 
    i+=1
    #print i,line
f = open("output.txt", "w")
#export all the words 
for word in words:
    f.write(word.encode("gbk"))
    f.write('\n'.encode("gbk"))
f.close()
    
  
