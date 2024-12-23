from collections import deque

def get_total_cost(farm):
    n = len(farm)
    m = len(farm[0])

    def in_bounds(r, c):
        return (0 <= r < n) and (0 <= c < m)

    def get_val(r, c):
        return farm[r][c]

    def get_neighbours(r, c):
        neighbours = []
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for (dr, dc) in dirs:
            neighbours.append((r + dr, c + dc))

        return [neighbour for neighbour in neighbours if in_bounds(neighbour[0], neighbour[1])]

    def get_val_neighbours(r, c):
        neighbours = get_neighbours(r, c)
        return [neighbour for neighbour in neighbours if get_val(neighbour[0], neighbour[1]) == get_val(r, c)]

    def get_region(r, c):
        visited = set()
        region = set()
        queue = deque([(r, c)])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                region.add(node)
                neighbours = get_val_neighbours(node[0], node[1])
                neighbours = [neighbour for neighbour in neighbours if neighbour not in visited]
                queue.extend(neighbours)
        return region
    
    def calc_edges(region):
        edges = 0
        for (r, c) in region:
            if ((r - 1, c) not in region):
                if not (((r, c - 1) in region) and ((r - 1, c - 1) not in region)):
                    edges += 1

            if ((r + 1, c) not in region):
                if not (((r, c - 1) in region) and ((r + 1, c - 1) not in region)):
                    edges += 1

            if ((r, c - 1) not in region):
                if not (((r - 1, c) in region) and ((r - 1, c - 1) not in region)):
                    edges += 1

            if ((r, c + 1) not in region):
                if not (((r - 1, c) in region) and ((r - 1, c + 1) not in region)):
                    edges += 1
        return edges

    regions = []
    visited = set()
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                region = get_region(i, j)
                visited |= region
                regions.append(region)

    cost = 0
    for region in regions:
        nextRegion = next(iter(region))
        val = get_val(nextRegion[0], nextRegion[1])
        area = len(region)
        edges = calc_edges(region)
        price = area * edges
        cost += price

    return cost

if __name__ == "__main__":
    # Open file 'day12-2.txt' in read mode
    with open('day12-2.txt', 'r') as f:
        farm = []
        for line in f:
            farm.append(line.strip())
        print("Total fencing cost: "  + str(get_total_cost(farm)))