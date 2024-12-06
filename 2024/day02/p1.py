data = open("d1.txt", "r").read().split("\n")

runic = data[0].split(":")[1].split(",")
sentence = data[2]

total = 0

for word in runic :
    for i in range(len(sentence)) :
        if sentence[i:].startswith(word) :
            total += 1

print(total)