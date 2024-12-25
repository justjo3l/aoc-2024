def check_count(towels, pattern, cache):
    if pattern == "":
        return 1

    if (block := cache.get(pattern, None)) is not None:
        return block

    result = 0
    for towel in towels:
        if towel == pattern[:len(towel)]:
            result += check_count(towels, pattern[len(towel):], cache)

    cache[pattern] = result
    return result

def get_num_achievable_patterns(towels, patterns):
    return sum([check_count(towels, pattern, {}) for pattern in patterns])

if __name__ == "__main__":
    towels = []
    patterns = []
    # Open file 'day19-2.txt' in read mode
    with open('day19-2.txt', 'r') as f:
        vals = []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            if len(towels) == 0:
                towels = line.split(', ')
            else:
                patterns.append(line)

        print("Number of ways to acheive patterns:", get_num_achievable_patterns(towels, patterns))