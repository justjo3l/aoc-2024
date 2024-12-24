from heapq import heappop, heappush

def get_lowest_score(maze):
    m = len(maze)
    n = len(maze[0])
    start = (-1, -1)
    end = (-1, -1)
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    maze[end[0]][end[1]] = '.'
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    heap = [(0, 0, *start)]

    while heap:
        score, dI, i, j = heappop(heap)
        if (i, j) == end:
            break

        if (dI, i, j) in visited:
            continue

        visited.add((dI, i, j))

        x = i + dirs[dI][0]
        y = j + dirs[dI][1]

        if maze[x][y] == '.' and (dI, x, y) not in visited:
            heappush(heap, (score + 1, dI, x, y))

        left = (dI - 1) % 4
        if (left, i, j) not in visited:
            heappush(heap, (score + 1000, left, i, j))

        right = (dI + 1) % 4
        if (right, i, j) not in visited:
            heappush(heap, (score + 1000, right, i, j))
        
    return score

if __name__ == "__main__":
    # Open file 'day16-1.txt' in read mode
    with open('day16-1.txt', 'r') as f:
        maze = []
        for line in f:
            line = line.strip()
            maze.append(list(line))

        print("Lowest Score:", get_lowest_score(maze))