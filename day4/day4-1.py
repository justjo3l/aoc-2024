def get_xmas_count(grid):
    n = len(grid[0])
    m = len(grid)
    i = 0
    j = 0
    numXmas = 0
    while i < m:
        j = 0
        while j < n:
            if grid[i][j] == "X" or grid[i][j] == "S":
                if j > 2 and i < m - 3:
                    currLeftDiagonal = grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3]
                    if currLeftDiagonal == "XMAS" or currLeftDiagonal == "SAMX":
                        numXmas += 1
                if j < n - 3 and i < m - 3:
                    currRightDiagonal = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3]
                    if currRightDiagonal == "XMAS" or currRightDiagonal == "SAMX":
                        numXmas += 1
                if i < m - 3:
                    currVertical = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]
                    if currVertical == "XMAS" or currVertical == "SAMX":
                        numXmas += 1
                if j < n - 3:
                    currHorizontal = grid[i][j:j+4]
                    if currHorizontal == "XMAS" or currHorizontal == "SAMX":
                        numXmas += 1
                        j += 2
            j += 1
        i += 1
    return numXmas

if __name__ == "__main__":
    list1 = []
    list2 = []
    # Open file 'day4-1.txt' in read mode
    with open('day4-1.txt', 'r') as f:
        # Read each line of the file
        grid = []
        for line in f:
            grid.append(line.strip())
        print("XMAS count: "  + str(get_xmas_count(grid)))