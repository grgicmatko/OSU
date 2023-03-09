fhand=open("SMSSpamCollection.txt", encoding="utf8")
hamLines=0
hamWords=0
spamLines=0
spamWords=0
count=0

for line in fhand:
    line = line.rstrip()
    words = line.split()

    if words[0]=="ham":
        hamLines+=1
        hamWords+=len(words)-1
        
    else:
        spamLines+=1
        spamWords+=len(words)-1
        
        if words[len(words)-1].endswith("!"):
            count+=1 

print(hamWords/hamLines)
print(spamWords/spamLines)
print(count)
fhand.close()