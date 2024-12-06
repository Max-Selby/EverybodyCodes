import statistics

data = open("d3.txt", "r").read()
nails = data.split("\n")
nails = [int(x) for x in nails]

mediann = int(round(statistics.median(nails)))
totalStrikes = 0

totals = [abs(x - mediann) for x in nails]

print(sum(totals))