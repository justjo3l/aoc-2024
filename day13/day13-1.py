def get_cheapest(machine):
    A = machine[0]
    B = machine[1]
    prize = machine[2]

    max_b = int(min(prize[0] / B[0], prize[1] / B[1]))

    for b in range(max_b, -1, -1):
        a = 0
        bv = (B[0] * b, B[1] * b)
        while ((A[0] * a) + bv[0], (A[1] * a) + bv[1]) < prize:
            a += 1

        if ((A[0] * a) + bv[0], (A[1] * a) + bv[1]) == prize:
            return b + (a * 3)

    return 0


def get_fewest_tokens(machines):
    tokens = 0
    for machine in machines:
        tokens += get_cheapest(machine)
    return tokens

if __name__ == "__main__":
    # Open file 'day13-1.txt' in read mode
    with open('day13-1.txt', 'r') as f:
        machines = []
        A = (0, 0)
        B = (0, 0)
        prize = (0, 0)
        for i, line in enumerate(f):
            line = line.strip()
            if i % 4 == 0:
                A = (int(line[line.find('+') + 1: line.find(',')]), int(line[line.find(',') + 4:]))
            elif i % 4 == 1:
                B = (int(line[line.find('+') + 1: line.find(',')]), int(line[line.find(',') + 4:]))
            elif i % 4 == 2:
                prize = (int(line[line.find('=') + 1: line.find(',')]), int(line[line.find(',') + 4:]))
                machines.append([
                    A,
                    B,
                    prize
                ])
            else:
                A = (0, 0)
                B = (0, 0)
                prize = (0, 0)

        print("Fewest number of tokens: "  + str(get_fewest_tokens(machines)))