def get_cheapest(machine):
    A = machine[0]
    B = machine[1]
    prize = (machine[2][0] + 10000000000000, machine[2][1] + 10000000000000)

    af = (A[1] / A[0])
    bf = (B[1] / B[0])

    xIntersection = round((prize[0] * af - prize[1]) / (af - bf))
    if xIntersection % B[0] != 0:
        return 0

    b = xIntersection // B[0]
    rem = ((prize[0] - B[0] * b), (prize[1] - B[1] * b))
    if rem[0] % A[0] != 0:
        return 0

    a = rem[0] // A[0]
    if ((B[0] * b) + (A[0] * a) == prize[0] and (B[1] * b) + (A[1] * a)) == prize[1]:
        return b + (a * 3)

    return 0


def get_fewest_tokens(machines):
    tokens = 0
    for machine in machines:
        tokens += get_cheapest(machine)
    return tokens

if __name__ == "__main__":
    # Open file 'day13-2.txt' in read mode
    with open('day13-2.txt', 'r') as f:
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