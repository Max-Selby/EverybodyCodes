data = open("d3.txt", "r").read().split("\n")

runic = data[0].split(":")[1].split(",")
runic.extend([word[::-1] for word in runic])
runic = set(runic) # to remove duplicates
grid = data[2:]

used = set()

for word in runic :
    for idx, line in enumerate(grid) :
        for jdx, _ in enumerate(line) :
            rightline = line[jdx:]+line
            if rightline.startswith(word) :
                spaces = range(jdx, jdx + len(word))
                for space in spaces :
                    used.add((idx, space % len(line)))
            downline = [d[jdx] for d in grid[idx:]]
            downline = "".join(downline)
            if downline.startswith(word) :
                spaces = range(idx, idx + len(word))
                for space in spaces :
                    used.add((space, jdx))

print(len(used))