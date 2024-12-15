def print_grid(grid):
    for row in grid:
        for val in row:
            print(val, end=' ')
        print()

def get_possible_obstacles(grid):
    n = len(grid)
    m = len(grid[0])
    gr = 0
    gc = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dirIndex = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                gr = i
                gc = j
                dirIndex = 0
            elif grid[i][j] == ">":
                gr = i
                gc = j
                dirIndex = 1
            elif grid[i][j] == "v":
                gr = i
                gc = j
                dirIndex = 2
            elif grid[i][j] == "<":
                gr = i
                gc = j
                dirIndex = 3

    numObstacles = 0
    for i in range(n):
        for j in range(m):
            r, c = gr, gc
            dirIndex = 0
            visited = set()
            while True:
                if (r, c, dirIndex) in visited:
                    numObstacles += 1
                    break
                visited.add((r, c, dirIndex))
                r += dirs[dirIndex][0]
                c += dirs[dirIndex][1]
                if not (0<=r<n and 0 <=c<m):
                    break
                if grid[r][c] == "#" or r == i and c == j:
                    r -= dirs[dirIndex][0]
                    c -= dirs[dirIndex][1]
                    dirIndex = (dirIndex + 1) % 4

    return numObstacles

if __name__ == "__main__":
    # Open file 'day6-2.txt' in read mode
    with open('day6-2.txt', 'r') as f:
        # Read each line of the file
        grid = []
        for line in f:
            grid.append(line.strip())
        print("Number of possible obstacles: "  + str(get_possible_obstacles(grid)))