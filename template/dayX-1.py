def get_answer(vals):
    print(vals)
    return 0

if __name__ == "__main__":
    # Open file 'dayX-1.txt' in read mode
    with open('dayX-1.txt', 'r') as f:
        vals = []
        for line in f:
            line = line.strip()
            vals.append(line)

        print("Answer: ", get_answer(vals))