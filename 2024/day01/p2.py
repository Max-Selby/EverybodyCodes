data = open("d2.txt", "r").read()

total = 0

total += data.count("B")
total += data.count("C") * 3
total += data.count("D") * 5

for idx in range(0, len(data), 2) :
    if not "x" in data[idx:][:2] :
        total += 2

print(total)