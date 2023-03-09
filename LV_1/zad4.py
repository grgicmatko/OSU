dic = {}
hamMessages=0
hamWords =0
spamMessages
fhand = open("SMSSpamCollection.txt")
for line in fhand:
    line =  line.strip()
    words = line.split()

    
fhand.close()
print(dic)
