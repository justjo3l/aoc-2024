def blink(stones):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
            continue
        n = len(str(stone))
        if n % 2 == 0:
            newStones.append(int(str(stone)[:(n//2)]))
            newStones.append(int(str(stone)[(n//2):]))
            continue
        newStones.append(stone * 2024)
    return newStones

def get_num_stones(stones):
    for _ in range(25):
        stones = blink(stones)
    return len(stones)

if __name__ == "__main__":
    # Open file 'day11-1.txt' in read mode
    with open('day11-1.txt', 'r') as f:
        stones = []
        for line in f:
            stones = [int(val) for val in line.strip().split()]
        print("Number of Stones: "  + str(get_num_stones(stones)))