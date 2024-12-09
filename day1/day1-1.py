def get_diff_sum(list1, list2):
    list1.sort()
    list2.sort()
    return sum([abs(list1[i] - list2[i]) for i in range(len(list1))])

if __name__ == "__main__":
    list1 = []
    list2 = []
    # Open file 'day1-1.txt' in read mode
    with open('day1-1.txt', 'r') as f:
        # Read each line of the file
        for line in f:
            nums = line.split()
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))

        result = get_diff_sum(list1, list2)
        print("Total Distance between lists: "  + str(result))