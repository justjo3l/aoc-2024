def check(towels, pattern, index):
    if index == len(pattern):
        return True

    for towel in towels:
        if towel == pattern[index:index+len(towel)]:
            if check(towels, pattern, index+len(towel)):
                return True

    return False

def get_num_possible_patterns(towels, patterns):
    return sum([1 for pattern in patterns if check(towels, pattern, 0)])

if __name__ == "__main__":
    towels = []
    patterns = []
    # Open file 'day19-1.txt' in read mode
    with open('day19-1.txt', 'r') as f:
        vals = []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            if len(towels) == 0:
                towels = line.split(', ')
            else:
                patterns.append(line)

        print("Number of possible patterns:", get_num_possible_patterns(towels, patterns))