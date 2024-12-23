a = 0
p = 0
accountedFarm = [[]]
n = 0
m = 0

def in_bounds(i, j):
    return i >= 0 and i < n and j >= 0 and j < m

def mark_plot(i, j, farm, type):
    global accountedFarm
    accountedFarm[i][j] = True
    global a
    a += 1
    numSides = 0
    if in_bounds(i - 1, j) and farm[i - 1][j] == type:
        numSides += 1
        if not accountedFarm[i - 1][j]:
            mark_plot(i - 1, j, farm, type)
    if in_bounds(i + 1, j) and farm[i + 1][j] == type:
        numSides += 1
        if not accountedFarm[i + 1][j]:
            mark_plot(i + 1, j, farm, type)
    if in_bounds(i, j - 1) and farm[i][j - 1] == type:
        numSides += 1
        if not accountedFarm[i][j - 1]:
            mark_plot(i, j - 1, farm, type)
    if in_bounds(i, j + 1) and farm[i][j + 1] == type:
        numSides += 1
        if not accountedFarm[i][j + 1]:
            mark_plot(i, j + 1, farm, type)
    global p
    p += (4 - numSides)

def calculate_region_cost(i, j, farm):
    global a
    a = 0
    global p
    p = 0
    type = farm[i][j]
    mark_plot(i, j, farm, type)
    cost = a * p
    return cost

def get_total_cost(farm):
    global n
    n = len(farm)
    global m
    m = len(farm[0])
    a = 0
    p = 0
    global accountedFarm
    accountedFarm = [[False for _ in range(m)] for _ in range(n)]
    cost = 0
    for i in range(n):
        for j in range(m):
            if not accountedFarm[i][j]:
                cost += calculate_region_cost(i, j, farm)
    return cost

if __name__ == "__main__":
    # Open file 'day12-1.txt' in read mode
    with open('day12-1.txt', 'r') as f:
        farm = []
        for line in f:
            farm.append(line.strip())
        print("Total fencing cost: "  + str(get_total_cost(farm)))