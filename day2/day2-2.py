def is_safe_report(report):
    negCount = len([num for num in report[1:] if num <= -1 and num >= -3])
    posCount = len([num for num in report[1:] if num >= 1 and num <= 3])
    if negCount == len(report[1:]):
        return -1, True
    elif posCount == len(report[1:]):
        return 1, True
    else:
        return (-1 if negCount > posCount else 1), False

def get_safe_count(reports):
    safeReports = 0
    for report in reports:
        prev = report[0]
        for i in range(1, len(report)):
            temp = report[i]
            report[i] = report[i] - prev
            prev = temp
        report[0] = 0
        gradient, is_safe = is_safe_report(report)
        if is_safe:
            safeReports += 1
            continue

        is_safe1 = False
        is_safe2 = False

        for i in range(1, len(report)):
            if gradient < 0 and (report[i] > -1 or report[i] < -3):
                if i == 1:
                    _, is_safe1 = is_safe_report(report[1:])
                    _, is_safe2 = is_safe_report(report[:1] + report[2:])
                    if is_safe1 or is_safe2:
                        safeReports += 1
                        break
                if i == len(report) - 1:
                    report = report[:-1]
                    break
                report[i] = report[i] + report[i + 1]
                report = report[:i+1] + report[i+2:]
                break
            elif gradient > 0 and (report[i] < 1 or report[i] > 3):
                if i == 1:
                    _, is_safe1 = is_safe_report(report[1:])
                    _, is_safe2 = is_safe_report(report[:1] + report[2:])
                    if is_safe1 or is_safe2:
                        safeReports += 1
                        break
                if i == len(report) - 1:
                    report = report[:-1]
                    break
                report[i] = report[i] + report[i + 1]
                report = report[:i+1] + report[i+2:]
                break
        if not is_safe1 and not is_safe2:
            gradient, is_safe = is_safe_report(report)

        if is_safe:
            safeReports += 1
            continue

    return safeReports

if __name__ == "__main__":
    list1 = []
    list2 = []
    # Open file 'day2-2.txt' in read mode
    with open('day2-2.txt', 'r') as f:
        # Read each line of the file
        reports = []
        for line in f:
            nums = line.split()
            reports.append([int(num) for num in nums])

        result = get_safe_count(reports)
        print("Number of safe reports: "  + str(result))