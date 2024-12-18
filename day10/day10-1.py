def print_map(hikeMap):
    for row in hikeMap:
        for val in row:
            print(val, end= ' ')
        print()

def checkPath(i, j, hikeMap, n, m, target):
    possible = False
    val = hikeMap[i][j]
    if val == 9 and (i, j) == target:
        return True
    if i - 1 >= 0 and hikeMap[i - 1][j] == val + 1:
        possible = possible or checkPath(i - 1, j, hikeMap, n, m, target)
    if i + 1 < n and hikeMap[i + 1][j] == val + 1:
        possible = possible or checkPath(i + 1, j, hikeMap, n, m, target)
    if j - 1 >= 0 and hikeMap[i][j - 1] == val + 1:
        possible = possible or checkPath(i, j - 1, hikeMap, n, m, target)
    if j + 1 < m and hikeMap[i][j + 1] == val + 1:
        possible = possible or checkPath(i, j + 1, hikeMap, n, m, target)
    return possible

def get_total_score(hikeMap):
    totalScore = 0
    trailHeads = []
    trailTails = []
    n = len(hikeMap)
    m = len(hikeMap[0])
    for i in range(n):
        for j in range(m):
            if hikeMap[i][j] == 0:
                trailHeads.append((i, j))
            elif hikeMap[i][j] == 9:
                trailTails.append((i, j))
    for trailHead in trailHeads:
        for trailTail in trailTails:
            if checkPath(trailHead[0], trailHead[1], hikeMap, n, m, trailTail):
                totalScore += 1
    return totalScore

if __name__ == "__main__":
    # Open file 'day10-1.txt' in read mode
    with open('day10-1.txt', 'r') as f:
        hikeMap = []
        for line in f:
            hikeMap.append([int(val) for val in line.strip()])
        print("Total score: "  + str(get_total_score(hikeMap)))