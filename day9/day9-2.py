def get_checksum(diskMap):
    checksum = 0

    vals = []
    space = []
    result = []
    id = 0
    pos = 0

    for i, val in enumerate(diskMap):
        if i % 2 == 0:
            vals.append((pos, int(val), id))
            for i in range(int(val)):
                result.append(id)
                pos += 1
            id += 1
        else:
            space.append((pos, int(val)))
            for i in range(int(val)):
                result.append(None)
                pos += 1

    for (currPos, currSize, currId) in reversed(vals):
        for spaceI, (spacePos, spaceSize) in enumerate(space):
            if spacePos < currPos and currSize <= spaceSize:
                for i in range(currSize):
                    result[currPos+i] = None
                    result[spacePos+i] = currId
                space[spaceI] = (spacePos + currSize, spaceSize - currSize)
                break

    i = 0
    for v in result:
        if v is not None:
            checksum += (i * v)
        i += 1
    return checksum

if __name__ == "__main__":
    # Open file 'day9-2.txt' in read mode
    with open('day9-2.txt', 'r') as f:
        diskMap = ""
        for line in f:
            diskMap = line.strip()
        print("Total checksum: "  + str(get_checksum(diskMap)))