def get_unique_positions(grid):
    n = len(grid)
    m = len(grid[0])
    guard = (0, 0)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dirIndex = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                guard = (i, j)
                dirIndex = 0
            elif grid[i][j] == ">":
                guard = (i, j)
                dirIndex = 1
            elif grid[i][j] == "v":
                guard = (i, j)
                dirIndex = 2
            elif grid[i][j] == "<":
                guard = (i, j)
                dirIndex = 3

    next_pos = guard
    uniquePositions = 0
    while next_pos[0] >= 0 and next_pos[0] < n and next_pos[1] >= 0 and next_pos[1] < m:
        next_pos = (guard[0] + dirs[dirIndex][0], guard[1] + dirs[dirIndex][1])
        if next_pos[0] < 0 or next_pos[0] >= n or next_pos[1] < 0 or next_pos[1] >= m:
            break
        if grid[guard[0]][guard[1]] != "X":
            uniquePositions += 1
            grid[guard[0]] = grid[guard[0]][:guard[1]] + "X" + grid[guard[0]][guard[1] + 1:]
        if grid[next_pos[0]][next_pos[1]] == "#":
            dirIndex = (dirIndex + 1) % 4
            next_pos = (guard[0] + dirs[dirIndex][0], guard[1] + dirs[dirIndex][1])
        guard = next_pos
    
    uniquePositions += 1
    grid[guard[0]] = grid[guard[0]][:guard[1]] + "X" + grid[guard[0]][guard[1] + 1:]

    return uniquePositions

if __name__ == "__main__":
    # Open file 'day6-1.txt' in read mode
    with open('day6-1.txt', 'r') as f:
        # Read each line of the file
        grid = []
        for line in f:
            grid.append(line.strip())
        print("Number of unique positions: "  + str(get_unique_positions(grid)))