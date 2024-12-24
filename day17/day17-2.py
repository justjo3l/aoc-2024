def run(regs, instructions):
    n = len(instructions)
    i = 0
    output = []
    def get_combo(operand):
        if 0 <= operand < 4:
            return operand
        elif operand == 4:
            return regs['a']
        elif operand == 5:
            return regs['b']
        elif operand == 6:
            return regs['c']
        return 0

    while i < n:
        curr = instructions[i]
        operand = instructions[i + 1]
        if curr == 0:
            regs['a'] //= 2**get_combo(operand)
        elif curr == 1:
            regs['b'] ^= operand
        elif curr == 2:
            regs['b'] = get_combo(operand) % 8
        elif curr == 3:
            if regs['a']:
                i = operand
                continue
        elif curr == 4:
            regs['b'] ^= regs['c']
        elif curr == 5:
            output.append(get_combo(operand) % 8)
        elif curr == 6:
            regs['b'] = regs['a'] // 2**get_combo(operand)
        elif curr == 7:
            regs['c'] = regs['a'] // 2**get_combo(operand)
        i += 2
    return list(output)

def get_lowest_a(regs, instructions):
    regs['a'] = 0
    j = 1
    iFloor = 0
    while j <= len(instructions) and j >= 0:
        regs['a'] <<= 3
        for i in range(iFloor, 8):
            regsCopy = regs.copy()
            regsCopy['a'] += i
            if instructions[-j:] == run(regsCopy, instructions):
                break
        else:
            j -= 1
            regs['a'] >>= 3
            iFloor = regs['a'] % 8 + 1
            regs['a'] >>= 3
            continue

        j += 1
        regs['a'] += i
        iFloor = 0

    return regs['a']

if __name__ == "__main__":
    regs = {}
    instructions = []
    # Open file 'day17-2.txt' in read mode
    with open('day17-2.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if regs.get('a') is None:
                regs['a'] = 0
            elif regs.get('b') is None:
                regs['b'] = int(line[line.find(':') + 2:])
            elif regs.get('c') is None:
                regs['c'] = int(line[line.find(':') + 2:])
            else:
                instructions = [int(val) for val in line[line.find(':') + 2:].split(',') if len(val) == 1]

        print("Lowest value of Register A:", get_lowest_a(regs, instructions))