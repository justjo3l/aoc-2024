def get_ordered_middle_sum(ruleLines, pageLines):
    ruleMap = dict()
    for line in ruleLines:
        pages = line.split('|')
        if ruleMap.get(pages[0]):
            ruleMap[pages[0]].append(pages[1])
        else:
            ruleMap[pages[0]] = [pages[1]]

    totalSum = 0
    indexMap = dict()
    for line in pageLines:
        nums = line.split(',')
        n = len(nums)
        mid = 0
        for i in range(n):
            curr = nums[i]
            if i == (n - 1) // 2:
                mid = curr
            indexMap[curr] = i
        valid = True
        for num in nums:
            if ruleMap.get(num):
                reqList = ruleMap[num]
                for req in reqList:
                    if indexMap.get(req) is not None and indexMap[num] > indexMap[req]:
                        valid = False
                        break
        if valid:
            totalSum += int(mid)
        indexMap.clear()
    return totalSum

if __name__ == "__main__":
    list1 = []
    list2 = []
    # Open file 'day5-1.txt' in read mode
    with open('day5-1.txt', 'r') as f:
        # Read each line of the file
        ruleLines = []
        pageLines = []
        stageFlag = 0
        for line in f:
            if stageFlag == 0:
                if line == '\n':
                    stageFlag = 1
                    continue
                ruleLines.append(line.strip())
            else:
                pageLines.append(line.strip())
        print("Sum of Ordered list middle values: "  + str(get_ordered_middle_sum(ruleLines, pageLines)))