def get_mul_results(input):
    sum = 0
    i = 3
    first = ""
    second = ""
    progressFlag = 0
    n = len(input)
    while i < n:
        if i < n - 3 and input[i:i+4] == "do()":
            progressFlag = 0
            i += 4
        elif i < n - 6 and input[i:i+7] == "don't()":
            progressFlag = -1
            i += 7
        curr = input[i]
        if progressFlag == 0:
            if curr == "(" and input[i-3:i] == "mul":
                progressFlag = 1
        elif progressFlag == 1:
            if curr == ',':
                progressFlag = 2
            elif not curr.isnumeric():
                progressFlag = 0
                first = ""
            else:
                first += curr
        elif progressFlag == 2:
            if curr == ')':
                sum += int(first) * int(second)
                first = ""
                second = ""
                progressFlag = 0
            elif not curr.isnumeric():
                progressFlag = 0
                first = ""
                second = ""
            else:
                second += curr
        i += 1
    return sum

if __name__ == "__main__":
    list1 = []
    list2 = []
    # Open file 'day3-2.txt' in read mode
    with open('day3-2.txt', 'r') as f:
        # Read each line of the file
        input = ""
        for line in f:
            input += line
        print("Total Multiplications Result: "  + str(get_mul_results(input)))