def get_safe_count(reports):
    safeReports = 0
    for report in reports:
        gradient = 1 if report[0] < report[1] else -1
        prev = report[0]
        safe = True
        for val in report[1:]:
            diff = val - prev
            if (diff < 1 or diff > 3) and gradient > 0:
                safe = False
                continue
            elif (diff > -1 or diff < -3) and gradient < 1:
                safe = False
                continue
            prev = val

        if safe:
            safeReports += 1

    return safeReports

if __name__ == "__main__":
    list1 = []
    list2 = []
    # Open file 'day2-1.txt' in read mode
    with open('day2-1.txt', 'r') as f:
        # Read each line of the file
        reports = []
        for line in f:
            nums = line.split()
            reports.append([int(num) for num in nums])

        result = get_safe_count(reports)
        print("Number of safe reports: "  + str(result))