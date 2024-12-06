data = open("d3.txt", "r").read()

total = 0

total += data.count("B")
total += data.count("C") * 3
total += data.count("D") * 5

for idx in range(0, len(data), 3) :
    enemies = 3 - data[idx:][:3].count("x")
    if enemies == 2 :
        total += 2
    elif enemies == 3 :
        total += 6

print(total)