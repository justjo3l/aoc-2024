from heapq import heappop, heappush

def in_bounds(i, j, n):
    return 0 <= i < n and 0 <= j < n

def navigate(maze, n):
    start = (0, 0)
    end = (n - 1, n - 1)
    heap = [(0, start[0], start[1])]
    visited = set()

    reached = False

    while heap:
        score, i, j = heappop(heap)

        if (i, j) == end:
            reached = True
            break

        if (i, j) in visited:
            continue

        visited.add((i, j))

        if in_bounds(i, j+1, n) and maze[i][j+1] not in visited and maze[i][j+1] == '.':
            heappush(heap, (score + 1, i, j+1))

        if in_bounds(i+1, j, n) and maze[i+1][j] not in visited and maze[i+1][j] == '.':
            heappush(heap, (score + 1, i+1, j))

        if in_bounds(i, j-1, n) and maze[i][j-1] not in visited and maze[i][j-1] == '.':
            heappush(heap, (score + 1, i, j-1))

        if in_bounds(i-1, j, n) and maze[i-1][j] not in visited and maze[i-1][j] == '.':
            heappush(heap, (score + 1, i-1, j))

    return reached

def init_maze(bytes, n, numBytes):
    maze = [['.' for _ in range(n)] for _ in range(n)]
    for byte in bytes[:numBytes]:
        maze[byte[1]][byte[0]] = '#'
    return maze

def get_first_blocking_bytes(bytes):
    n = 71
    numBytes = 0
    maze = init_maze(bytes, n, 0)
    while navigate(maze, n):
        maze = init_maze(bytes, n, numBytes)
        numBytes += 1

    return bytes[numBytes - 2]

if __name__ == "__main__":
    # Open file 'day18-2.txt' in read mode
    with open('day18-2.txt', 'r') as f:
        bytes = []
        for line in f:
            line = line.strip()
            x, y = line.split(',')
            bytes.append((int(x), int(y)))

        print("First blocking byte:", get_first_blocking_bytes(bytes))