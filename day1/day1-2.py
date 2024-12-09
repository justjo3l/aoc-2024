def get_similarity_score(list1, list2):
    countMap = dict()
    for i in range(len(list2)):
        curr = list2[i]
        if countMap.get(curr) is None:
            countMap[curr] = 1
        else:
            countMap[curr] += 1

    ss = 0
    for i in range(len(list1)):
        curr = list1[i]
        ss += curr * (countMap.get(curr) or 0)

    return ss

if __name__ == "__main__":
    list1 = []
    list2 = []
    # Open file 'day1-2.txt' in read mode
    with open('day1-2.txt', 'r') as f:
        # Read each line of the file
        for line in f:
            nums = line.split()
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))

        result = get_similarity_score(list1, list2)
        print("Similarity Score: "  + str(result))