from collections import deque

def find_start(grid, n, m):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                return (i, j)
    return (0, 0)

def in_bounds(i, j, n, m):
    return (0 <= i < n) and (0 <= j < m)

def move(grid, loc, dir, n, m):
    curr = (loc[0], loc[1])
    addStack = deque()
    addStack.append('@')
    while True:
        newPos = (curr[0] + dir[0], curr[1] + dir[1])
        if in_bounds(newPos[0], newPos[1], n, m):
            val = grid[newPos[0]][newPos[1]]
            if val == '#':
                return loc
            elif val == 'O':
                addStack.append('O')
            elif val == '.':
                revDir = (-dir[0], -dir[1])
                while addStack:
                    movedVal = addStack.pop()
                    grid[newPos[0]] = grid[newPos[0]][:newPos[1]] + movedVal + grid[newPos[0]][newPos[1] + 1:]
                    newPos = (newPos[0] + revDir[0], newPos[1] + revDir[1])
                grid[loc[0]] = grid[loc[0]][:loc[1]] + '.' + grid[loc[0]][loc[1] + 1:]
                return (loc[0] + dir[0], loc[1] + dir[1])
        else:
            return loc
        curr = (newPos[0], newPos[1])


def get_box_coords(grid, instructions):
    n = len(grid)
    m = len(grid[0])
    loc = find_start(grid, n, m)

    dirMap = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    for instruction in instructions:
        loc = move(grid, loc, dirMap.get(instruction), n, m)

    total = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                total += ((100 * i) + j)
    return total

if __name__ == "__main__":
    # Open file 'day15-1.txt' in read mode
    with open('day15-1.txt', 'r') as f:
        grid = []
        ended = False
        instructions = []
        for line in f:
            if line == '\n':
                ended = True
            line = line.strip()
            if not ended:
                grid.append(line)
            else:
                instructions.extend(list(line))

        print("Final Coordinates of Boxes: "  + str(get_box_coords(grid, instructions)))