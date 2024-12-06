data = open("d2.txt", "r").read().split("\n")

runic = data[0].split(":")[1].split(",")
sentences = data[2:]

total = 0

for sentence in sentences :
    chosen = set()
    i = 0
    while i < len(sentence) :
        for word in runic :
            if sentence[i:].startswith(word) or sentence[i:].startswith(word[::-1]) :
                chosen.update(list(range(i, i + len(word))))
        i += 1
    total += len(chosen)

print(total)