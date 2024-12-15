def tern(num):
    if num == 0:
        return "0"
    nums = []
    while num:
        num, rem = divmod(num, 3)
        nums.append(str(rem))
    return ''.join(reversed(nums))

def equation_calc(vals, ops, n):
    result = vals[0]
    for i in range(1, n):
        if ops[i - 1] == 0:
            result += vals[i]
        elif ops[i - 1] == 1:
            result *= vals[i]
        else:
            result = int(str(result) + str(vals[i]))
    return result

def check_valid_equation(testVal, vals):
    n = len(vals)
    ops = [0 for _ in range(n - 1)]
    iNum = 0
    while True:
        if testVal == equation_calc(vals, ops, n):
            return testVal
        if n == ops.count(2) + 1:
            return 0
        iNum += 1
        ops = [int(d) for d in str(tern(iNum))[2:]]
        opsN = len(ops)
        ops = [0 for _ in range(n - 1 - opsN)] + ops



def get_total_valid_sum(equations):
    validSum = 0

    for (k, v) in equations:
        validSum += check_valid_equation(k, v)

    return validSum

if __name__ == "__main__":
    # Open file 'day7-2.txt' in read mode
    with open('day7-2.txt', 'r') as f:
        # Read each line of the file
        equations = list()
        for line in f:
            vals = line.split()
            equations.append((int(vals[0][:-1]), [int(val) for val in vals[1:]]))
        print("Sum of valid test values: "  + str(get_total_valid_sum(equations)))