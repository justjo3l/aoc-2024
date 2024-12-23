import math

def calculate_quadrants(r, c, grid):
    rh = r // 2
    ch = c // 2
    qs = [0, 0, 0, 0]
    for i in range(r):
        for j in range(c):
            curr = grid[i][j]
            if curr.isnumeric():
                if i < rh:
                    if j < ch:
                        qs[0] += int(curr)
                    elif j == ch:
                        continue
                    else:
                        qs[1] += int(curr)
                elif i == rh:
                    continue
                else:
                    if j < ch:
                        qs[3] += int(curr)
                    elif j == ch:
                        continue
                    else:
                        qs[2] += int(curr)
    return math.prod(qs)

def get_safety_score(r, c, robots):
    new_grid = [['.' for _ in range(c)] for _ in range(r)]
    for robot in robots:
        robot[0] = (robot[0] + (100 * robot[2])) % r
        robot[1] = (robot[1] + (100 * robot[3])) % c
        curr = new_grid[robot[0]][robot[1]]
        if curr.isnumeric():
            new_grid[robot[0]][robot[1]] = str(int(curr) + 1)
        else:
            new_grid[robot[0]][robot[1]] = '1'
    return calculate_quadrants(r, c, new_grid)

if __name__ == "__main__":
    # Open file 'day14-1.txt' in read mode
    r = 103
    c = 101
    with open('day14-1.txt', 'r') as f:
        robots = []
        for line in f:
            line = line.strip()
            p = line[line.find("p=") + 2:line.find(" v=")].split(',')
            p.reverse()
            v = line[line.find("v=") + 2:].split(',')
            v.reverse()
            p.extend(v)
            robots.append([int(val) for val in p])

        print("Safety Score: "  + str(get_safety_score(r, c, robots)))