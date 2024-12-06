data = open("d3.txt", "r").read()
grid = data.split("\n")
grid = [list(s) for s in grid]
total = 0

def counts(grid) :
    t = 0
    for line in grid :
        t += line.count("#")
    return t

while counts(grid) > 0 :
    total += counts(grid)
    
    newGrid = []
    for i in range(len(grid)) :
        line = []
        for j in range(len(grid[0])) :
            line.append(".")
        newGrid.append(line)
    
    for idx, line in enumerate(grid) :
        for jdx, _ in enumerate(line) :
            if idx == 0 or idx == len(grid) - 1 or jdx == 0 or jdx == len(line) - 1 :
                continue
            cardinalSafe = grid[idx - 1][jdx] == "#" and grid[idx + 1][jdx] == "#" and grid[idx][jdx - 1] == "#" and grid[idx][jdx + 1] == "#"
            diagSafe = grid[idx - 1][jdx - 1] == "#" and grid[idx - 1][jdx + 1] == "#" and grid[idx + 1][jdx - 1] == "#" and grid[idx + 1][jdx + 1] == "#"
            spotSafe = grid[idx][jdx] == "#"
            if cardinalSafe and diagSafe and spotSafe :
                newGrid[idx][jdx] = "#"
    grid = newGrid

print(total)