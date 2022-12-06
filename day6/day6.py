INPUT_FILE = "input.txt"

def part1():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    line = lines[0]
    chars = {}

    for i in range(len(line)):
        if line[i] in chars:
            ind = chars[line[i]]
            charsCopy = chars.copy()
            for char in charsCopy:
                if charsCopy[char] <= ind:
                    chars.pop(char)
        chars[line[i]] = i
        if len(chars) == 4:
            print(chars)
            print(i+1)
            return i + 1

def part2():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    line = lines[0]
    chars = {}

    for i in range(len(line)):
        if line[i] in chars:
            ind = chars[line[i]]
            charsCopy = chars.copy()
            for char in charsCopy:
                if charsCopy[char] <= ind:
                    chars.pop(char)
        chars[line[i]] = i
        if len(chars) == 14:
            print(chars)
            print(i+1)
            return i + 1

if __name__ == '__main__':
    part2()