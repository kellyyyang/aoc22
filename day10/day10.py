INPUT_FILE = 'input.txt'
FILL_CHAR = '██'
EMPTY_CHAR = '░░'

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
                result += (cycle+1)*x_val
            cycle += 1
            x_val += num
        if (cycle - 20 + 1) % 40 == 0 and cycle <= 220:
            result += (cycle+1) * x_val
    return result

def part2():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    x_val = 1
    sprite_pos = 1
    crt_pos = -1
    result = ""
    cycle = 0

    for line in lines:
        line = line.split()
        if len(line) > 1:
            instruct, num = line[0], int(line[1])
        else:
            instruct = line[0]

        if instruct == 'noop':
            cycle += 1
            crt_pos += 1
            if (crt_pos - 40) == 0:
                crt_pos = 0
                result += '\n'
            if abs(sprite_pos - crt_pos) <= 1:
                result += FILL_CHAR
            else:
                result += EMPTY_CHAR

        elif instruct == 'addx':
            cycle += 1
            crt_pos += 1
            if (crt_pos - 40) == 0:
                crt_pos = 0
                result += '\n'
            if abs(sprite_pos - crt_pos) <= 1:
                result += FILL_CHAR
            else:
                result += EMPTY_CHAR

            cycle += 1
            crt_pos += 1
            if (crt_pos - 40) == 0:
                crt_pos = 0
                result += '\n'
            if abs(sprite_pos - crt_pos) <= 1:
                result += FILL_CHAR
            else:
                result += EMPTY_CHAR

            x_val += num
            sprite_pos = x_val
        
    return result

if __name__ == '__main__':
    print(part2())
