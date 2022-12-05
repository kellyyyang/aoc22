INPUT_FILE = "input.txt"

def part1():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    result = 0

    for line in lines:
        newLine = line.split(',')
        
        start1, end1 = int(newLine[0].split('-')[0]), int(newLine[0].split('-')[1])
        start2, end2 = int(newLine[1].split('-')[0]), int(newLine[1].split('-')[1])

        # second is fully contained in first
        if start1 <= start2 and end1 >= end2:
            result += 1
        # first is fully contained in second
        elif start2 <= start1 and end2 >= end1:
            result += 1
        # second is slightly less than first
        elif start1 <= end2 and end1 >= start2:
            result += 1
        # first is slightly less than second
        elif start2 <= end1 and end2 >= start1:
            result += 1

    return result


if __name__ == "__main__":
    print(part1())
    # part1()