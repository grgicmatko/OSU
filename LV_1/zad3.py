
list = []
while 1:
    word = input()
    if word.isdigit():
        list.append(int(word))
    elif word == "Done":
        break
    else:
        print("NaN")
        continue

print(len(list))
print(sum(list)/len(list))
print(min(list))
print(max(list))

list.sort()
print(list)


      