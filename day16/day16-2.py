from heapq import heappop, heappush

def get_num_seats(maze):
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
    visited = {}
    heap = [(0, 0, *start, {start})]
    lowest = 0
    winning_paths = set()

    def can_visit(score, dI, i, j):
        prevScore = visited.get((dI, i, j))
        if prevScore and prevScore < score:
            return False
        visited[(dI, i, j)] = score
        return True

    while heap:
        score, dI, i, j, path = heappop(heap)
        if lowest and lowest < score:
            break

        if (i, j) == end:
            lowest = score
            winning_paths |= path
            continue

        if not can_visit(score, dI, i, j):
            continue

        x = i + dirs[dI][0]
        y = j + dirs[dI][1]

        if maze[x][y] == '.' and can_visit(score + 1, dI, x, y):
            heappush(heap, (score + 1, dI, x, y, path | {(x, y)}))

        left = (dI - 1) % 4
        if can_visit(score + 1000, left, i, j):
            heappush(heap, (score + 1000, left, i, j, path))

        right = (dI + 1) % 4
        if can_visit(score + 1000, right, i, j):
            heappush(heap, (score + 1000, right, i, j, path))

    return len(winning_paths)

if __name__ == "__main__":
    # Open file 'day16-2.txt' in read mode
    with open('day16-2.txt', 'r') as f:
        maze = []
        for line in f:
            line = line.strip()
            maze.append(list(line))

        print("Number of seats:", get_num_seats(maze))