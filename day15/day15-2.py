from collections import defaultdict

def get_box_coords(grid, instructions):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in reversed(range(n)):
            if grid[i][j] == '#':
                grid[i].insert(j, '#')
            if grid[i][j] == '.':
                grid[i].insert(j, '.')
            if grid[i][j] == '@':
                robot = (i, j*2)
                grid[i][j:j+1] = ['.', '.']
            if grid[i][j] == 'O':
                grid[i][j:j+1] = ['[', ']']

    for d in instructions[:]:
        i, j = robot
        if d == '<':
            k = j-1
            while grid[i][k] == ']':
                k -= 2
            if grid[i][k] == '.':
                for l in range(k, j):
                    grid[i][l] = grid[i][l+1]
                robot = (i, j-1)

        elif d == '>':
            k = j+1
            while grid[i][k] == '[':
                k += 2
            if grid[i][k] == '.':
                for l in reversed(range(j+1, k+1)):
                    grid[i][l] = grid[i][l-1]
                robot = (i, j+1)

        elif d == '^':
            queue = {(i-1, j)}
            rows = defaultdict(set)
            while queue:
                x, y = queue.pop()
                match grid[x][y]:
                    case '#':
                        break
                    case ']':
                        rows[x] |= {y-1, y}
                        queue |= {(x-1, y), (x-1, y-1)}
                    case '[':
                        rows[x] |= {y, y+1}
                        queue |= {(x-1, y), (x-1, y+1)}
                    case '.':
                        rows[x].add(y)
            else:
                for x in sorted(rows):
                    for y in rows[x]:
                        grid[x][y] = grid[x+1][y] if y in rows[x+1] else '.'
                robot = (i-1, j)

        elif d== 'v':
            queue = {(i+1, j)}
            rows = defaultdict(set)
            while queue:
                x, y = queue.pop()
                match grid[x][y]:
                    case '#':
                        break
                    case ']':
                        rows[x] |= {y-1, y}
                        queue |= {(x+1, y), (x+1, y-1)}
                    case '[':
                        rows[x] |= {y, y+1}
                        queue |= {(x+1, y), (x+1, y+1)}
                    case '.':
                        rows[x].add(y)
            else:
                for x in sorted(rows, reverse=True):
                    for y in rows[x]:
                        grid[x][y] = grid[x-1][y] if y in rows[x-1] else '.'
                robot = (i+1, j)

    total = 0
    for i in range(m):
        for j in range(n*2):
            if grid[i][j] == '[':
                total += 100*i + j

    return total

if __name__ == "__main__":
    # Open file 'day15-2.txt' in read mode
    with open('day15-2.txt', 'r') as f:
        grid = []
        ended = False
        instructions = []
        for line in f:
            if line == '\n':
                ended = True
            line = line.strip()
            if not ended:
                grid.append(list(line))
            else:
                instructions.extend(list(line))

        print("Final Coordinates of Boxes: "  + str(get_box_coords(grid, instructions)))