output = ""
i = 0

def get_result_string(regs, instructions):
    global output
    n = len(instructions)
    global i

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

    def adv(operand):
        operand = get_combo(operand)
        regs['a'] = int(regs['a'] // (2**operand))
        return

    def bxl(operand):
        regs['b'] = int(regs['b'] ^ operand)
        return

    def bst(operand):
        operand = get_combo(operand)
        regs['b'] = int(operand % 8)
        return

    def jnz(operand):
        global i
        if regs['a'] != 0:
            i = int(operand) - 1
        return

    def bxc(operand):
        regs['b'] = int(regs['b'] ^ regs['c'])
        return

    def out(operand):
        global output
        operand = get_combo(operand)
        output += str(operand % 8)
        return

    def bdv(operand):
        operand = get_combo(operand)
        regs['b'] = int(regs['a'] // (2**operand))
        return

    def cdv(operand):
        operand = get_combo(operand)
        regs['c'] = int(regs['a'] // (2**operand))
        return

    while i < n:
        curr = instructions[i]
        if curr[0] == 0:
            adv(curr[1])
        elif curr[0] == 1:
            bxl(curr[1])
        elif curr[0] == 2:
            bst(curr[1])
        elif curr[0] == 3:
            jnz(curr[1])
        elif curr[0] == 4:
            bxc(curr[1])
        elif curr[0] == 5:
            out(curr[1])
        elif curr[0] == 6:
            bdv(curr[1])
        elif curr[0] == 7:
            cdv(curr[1])
        i += 1
    return ','.join(list(output))

if __name__ == "__main__":
    regs = {}
    instructions = []
    # Open file 'day17-1.txt' in read mode
    with open('day17-1.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if regs.get('a') is None:
                regs['a'] = int(line[line.find(':') + 2:])
            elif regs.get('b') is None:
                regs['b'] = int(line[line.find(':') + 2:])
            elif regs.get('c') is None:
                regs['c'] = int(line[line.find(':') + 2:])
            else:
                instructions = [int(val) for val in line[line.find(':') + 2:].split(',') if len(val) == 1]
                instructions = [(instructions[i], instructions[i + 1]) for i in range(0, len(instructions), 2)]

        print("Result String:", get_result_string(regs, instructions))