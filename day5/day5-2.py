def get_corrected_page(page, indexMap, ruleMap):
    i = 0
    n = len(page)
    while i < n:
        curr = page[i]
        if ruleMap.get(curr):
            reqList = ruleMap[curr]
            for req in reqList:
                currIndex = page.index(curr)
                if req in page:
                    reqIndex = page.index(req)
                else:
                    continue
                if indexMap.get(req) is not None and currIndex > reqIndex:
                    page.remove(req)
                    page = page[:(currIndex + 1)] + [req] + page[(currIndex + 1):]
                    i = -1
        i += 1
    return int(page[(n - 1) // 2])

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
        for i in range(n):
            curr = nums[i]
            indexMap[curr] = i
        valid = True
        for num in nums:
            if ruleMap.get(num):
                reqList = ruleMap[num]
                for req in reqList:
                    if indexMap.get(req) is not None and indexMap[num] > indexMap[req]:
                        valid = False
                        break
        if not valid:
            totalSum += get_corrected_page(nums, indexMap, ruleMap)
        indexMap.clear()
    return totalSum

if __name__ == "__main__":
    list1 = []
    list2 = []
    # Open file 'day5-2.txt' in read mode
    with open('day5-2.txt', 'r') as f:
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