def print_map(hikeMap):
    for row in hikeMap:
        for val in row:
            print(val, end= ' ')
        print()

def checkNumPaths(i, j, hikeMap, n, m, numPaths):
    uniquePaths = 0
    val = hikeMap[i][j]
    if val == 9:
        return 1
    if i - 1 >= 0 and hikeMap[i - 1][j] == val + 1:
        uniquePaths += checkNumPaths(i - 1, j, hikeMap, n, m, numPaths)
    if i + 1 < n and hikeMap[i + 1][j] == val + 1:
        uniquePaths += checkNumPaths(i + 1, j, hikeMap, n, m, numPaths)
    if j - 1 >= 0 and hikeMap[i][j - 1] == val + 1:
        uniquePaths += checkNumPaths(i, j - 1, hikeMap, n, m, numPaths)
    if j + 1 < m and hikeMap[i][j + 1] == val + 1:
        uniquePaths += checkNumPaths(i, j + 1, hikeMap, n, m, numPaths)
    return uniquePaths

def get_total_rating(hikeMap):
    totalRating = 0
    trailHeads = []
    n = len(hikeMap)
    m = len(hikeMap[0])
    for i in range(n):
        for j in range(m):
            if hikeMap[i][j] == 0:
                trailHeads.append((i, j))
    for trailHead in trailHeads:
        totalRating += checkNumPaths(trailHead[0], trailHead[1], hikeMap, n, m, 0)
    return totalRating

if __name__ == "__main__":
    # Open file 'day10-2.txt' in read mode
    with open('day10-2.txt', 'r') as f:
        hikeMap = []
        for line in f:
            hikeMap.append([-1 if val == '.' else int(val) for val in line.strip()])
        print("Total score: "  + str(get_total_rating(hikeMap)))