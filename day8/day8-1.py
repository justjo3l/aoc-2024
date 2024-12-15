def print_grid(grid):
    for row in grid:
        for val in row:
            print(val, end=' ')
        print()

def get_antenna_vals(grid, n, m):
    antennas = dict()
    for i in range(n):
        for j in range(m):
            curr = grid[i][j]
            if curr != '.':
                if antennas.get(curr) is not None:
                    antennas[curr].append((i, j))
                else:
                    antennas[curr] = [(i, j)]

    return antennas

def get_unique_antinode_num(grid):
    numAntinodes = 0
    n = len(grid)
    m = len(grid[0])
    antennas = get_antenna_vals(grid, n, m)
    for vals in antennas.values():
        valN = len(vals)
        for i in range(valN):
            for j in range(i + 1, valN):
                diff = (vals[i][0] - vals[j][0], vals[i][1] - vals[j][1])
                (r, c) = min(vals[i], vals[j])
                r += diff[0]
                c += diff[1]
                if 0<=r<n and 0<=c<m:
                    if grid[r][c] != "#":
                        grid[r] = grid[r][:c] + "#" + grid[r][c+1:]
                        numAntinodes += 1
                (r, c) = max(vals[i], vals[j])
                r -= diff[0]
                c -= diff[1]
                if 0<=r<n and 0<=c<m:
                    if grid[r][c] != "#":
                        grid[r] = grid[r][:c] + "#" + grid[r][c+1:]
                        numAntinodes += 1


    return numAntinodes

if __name__ == "__main__":
    # Open file 'day8-1.txt' in read mode
    with open('day8-1.txt', 'r') as f:
        # Read each line of the file
        grid = []
        for line in f:
            grid.append(line.strip())
        print("Number of unique antinode positions: "  + str(get_unique_antinode_num(grid)))