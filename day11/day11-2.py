cacheMap = dict()

def blink(stone, times):
    cached = cacheMap.get((stone, times))
    if cached is not None:
        return cached
    result = 0
    if times == 0:
        result = 1
    elif stone == 0:
        result = blink(1, times - 1)
    elif len(str(stone)) % 2 == 0:
        stoneStr = str(stone)
        n = len(stoneStr)
        left = stoneStr[:(n//2)]
        right = stoneStr[(n//2):]
        result = blink(int(left), times - 1) + blink(int(right), times - 1)
    else:
        result = blink(stone * 2024, times - 1)
    cacheMap[(stone, times)] = result
    return result

def get_num_stones(stones):
    numStones = 0
    for stone in stones:
        numStones += blink(stone, 75)
    return numStones

if __name__ == "__main__":
    # Open file 'day11-2.txt' in read mode
    with open('day11-2.txt', 'r') as f:
        stones = []
        for line in f:
            stones = [int(val) for val in line.strip().split()]
        print("Number of Stones: "  + str(get_num_stones(stones)))