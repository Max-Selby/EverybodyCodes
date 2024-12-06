data = open("d1.txt", "r").read()

total = 0

total += data.count("B")
total += data.count("C") * 3

print(total)