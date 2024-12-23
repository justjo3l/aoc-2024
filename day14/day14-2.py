def get_min_seconds(r, c, robots):
    seconds = 0
    while True:
        grid = [[0 for _ in range(c)] for _ in range(r)]
        seconds += 1
        flag = True

        for robot in robots:
            x = (robot[0] + robot[2] * seconds) % r
            y = (robot[1] + robot[3] * seconds) % c
            grid[x][y] += 1
            if grid[x][y] > 1:
                flag = False
        if flag:
            return seconds

if __name__ == "__main__":
    # Open file 'day14-2.txt' in read mode
    r = 103
    c = 101
    with open('day14-2.txt', 'r') as f:
        robots = []
        for line in f:
            line = line.strip()
            p = line[line.find("p=") + 2:line.find(" v=")].split(',')
            p.reverse()
            v = line[line.find("v=") + 2:].split(',')
            v.reverse()
            p.extend(v)
            robots.append([int(val) for val in p])

        print("Minimum number of seconds: "  + str(get_min_seconds(r, c, robots)))