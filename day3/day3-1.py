def get_mul_results(input):
    sum = 0
    i = 3
    first = ""
    second = ""
    progressFlag = 0
    while i < len(input):
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
    # Open file 'day3-1.txt' in read mode
    with open('day3-1.txt', 'r') as f:
        # Read each line of the file
        result = 0
        for line in f:
            result += get_mul_results(line)
        print("Total Multiplications Result: "  + str(result))