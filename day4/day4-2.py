def get_x_mas_count(grid):
    n = len(grid[0])
    m = len(grid)
    i = 0
    j = 0
    numXMas = 0
    acceptableValues = dict()
    acceptableValues["MS"] = True
    acceptableValues["SM"] = True
    while i < m:
        j = 0
        while j < n:
            if grid[i][j] == "A":
                if j > 0 and i > 0 and i < m - 1 and j < n - 1:
                    leftmas = grid[i-1][j-1] + grid[i+1][j+1]
                    rightmas = grid[i-1][j+1] + grid[i+1][j-1]
                    if acceptableValues.get(leftmas) and acceptableValues.get(rightmas):
                        numXMas += 1
            j += 1
        i += 1
    return numXMas

if __name__ == "__main__":
    list1 = []
    list2 = []
    # Open file 'day4-2.txt' in read mode
    with open('day4-2.txt', 'r') as f:
        # Read each line of the file
        grid = []
        for line in f:
            grid.append(line.strip())
        print("X-MAS count: "  + str(get_x_mas_count(grid)))