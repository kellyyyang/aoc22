INPUT_FILE = "input.txt"
test = False

def part1():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    numStacks = 9
    if test:
        numStacks = 3

    stacks = [[] for i in range(numStacks)]

    for line in lines:
        # we are looking at crates
        if len(line) >= 4 and line[:4] != "move":
            for i in range(len(line)):
                if line[i].isalpha():
                    stacks[i // 4].append(line[i])

        elif len(line) >= 4 and line[:4] == "move":
            fromStack = int(line[-7]) - 1
            toStack = int(line[-2]) - 1
            numBlocks = int(line[5:7])
            for i in range(numBlocks):
                block = stacks[fromStack].pop(0)
                stacks[toStack].insert(0, block)
    
    result = ''

    for stack in stacks:
        result += stack[0]

    print(result)

def part2():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    numStacks = 9
    if test:
        numStacks = 3

    stacks = [[] for i in range(numStacks)]

    for line in lines:
        # we are looking at crates
        if len(line) >= 4 and line[:4] != "move":
            for i in range(len(line)):
                if line[i].isalpha():
                    stacks[i // 4].append(line[i])

        elif len(line) >= 4 and line[:4] == "move":
            fromStack = int(line[-7]) - 1
            toStack = int(line[-2]) - 1
            numBlocks = int(line[5:7])
            blocks = stacks[fromStack][:numBlocks]
            stacks[toStack] = blocks + stacks[toStack]
            for i in range(numBlocks):
                stacks[fromStack].pop(0)
    
    result = ''

    for stack in stacks:
        result += stack[0]

    print(stacks)
    print(result)

if __name__ == '__main__':
    part2()