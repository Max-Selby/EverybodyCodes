data = open("d1.txt", "r").read()
nails = data.split("\n")
nails = [int(x) for x in nails]

smallest = sorted(nails)[0]
totalStrikes = 0

totals = [x - smallest for x in nails]
print(sum(totals))