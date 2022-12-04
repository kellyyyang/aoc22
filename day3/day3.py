INPUT_FILE = "day3_input.txt"

def part1():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    result = 0

    for line in lines:
        first_half = len(line) // 2

        read_chars_first = set()
        read_chars_second = set()

        for char in line[:first_half]:
            read_chars_first.add(char)
        for char in line[first_half:]:
            if char in read_chars_first and char not in read_chars_second:
                # print(line, char)
                if char == char.lower():
                    # print(ord(char) - 96)
                    result += ord(char) - 96
                else:
                    # print(ord(char) - 64)
                    result += ord(char) - 38
            read_chars_second.add(char)

    return result

def part2():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    result = 0
    count = 0

    read_chars_first = set()
    read_chars_second = set()

    for line in lines:
        count += 1
        if count % 3 == 1:
            for char in line:
                if char != '\n':
                    read_chars_first.add(char)
        elif count % 3 == 2:
            for char in line:
                if char in read_chars_first:
                    if char != '\n':
                        read_chars_second.add(char)
        else:
            for char in line:
                if char != '\n':
                    if char in read_chars_second:
                        # print(char)
                        if char == char.lower():
                            result += ord(char) - 96
                        else:
                            result += ord(char) - 38
                        # print(result)
                        break
            read_chars_first.clear()
            read_chars_second.clear()

    return result
                    

if __name__ == "__main__":
    print(part2())