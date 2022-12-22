INPUT_FILE = 'input.txt'

def part1():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    cycle = 0
    x_val = 1
    result = 0

    for line in lines:
        line = line.split()
        if len(line) > 1:
            instruct, num = line[0], int(line[1])
        else:
            instruct = line[0]

        if instruct == 'noop':
            cycle += 1
        elif instruct == 'addx':
            cycle += 1
            if (cycle - 20 + 1) % 40 == 0 and cycle < 221:
                # print("second", cycle+1)
                result += (cycle+1)*x_val
                # print((cycle+1)*x_val)
            cycle += 1
            x_val += num
        if (cycle - 20 + 1) % 40 == 0 and cycle <= 220:
            # print("third", cycle+1)
            result += (cycle+1) * x_val
            # print((cycle+1)*x_val)
    return result

if __name__ == '__main__':
    print(part1())
