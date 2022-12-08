INPUT_FILE = "input.txt"

def part1():
    f = open(INPUT_FILE)
    lines = f.readlines()[1:]
    f.close()

    dirs = {'/':0}
    levels = {0: ['/']}
    currLevel = 0
    currPath = ['/']
    nested = {}

    for line in lines:
        if len(line) > 4 and line[:4] == "$ cd":
            currDir = line[5:][:-1]
            if currDir != "..":
                currPath.append(currDir)
                if len(currPath) > 1:
                    currPathStrFirst = '/'.join(currPath)[1:]
                else:
                    currPathStrFirst = '/'
                currLevel += 1

                if currPathStrFirst not in dirs:
                    dirs[currPathStrFirst] = 0

                if currLevel not in levels:
                    levels[currLevel] = [currPathStrFirst]
                else:
                    levels[currLevel].append(currPathStrFirst)
            
            else:
                currLevel -= 1
                currPath.pop()

        elif len(line) > 1 and line[0] != '$':
            if (len(line) >= 3 and line[:3] == 'dir'): # line containing file size and file name
                if len(currPath) > 1:
                    currPathStrH = '/'.join(currPath)[1:]
                else:
                    currPathStrH = '/'
                if currPathStrH in nested:
                    if currPathStrH != '/':
                        nested[currPathStrH].append(currPathStrH + '/' + line[4:][:-1])
                    else:
                        nested[currPathStrH].append(currPathStrH + line[4:][:-1])
                else:
                    if currPathStrH != '/':
                        nested[currPathStrH] = [currPathStrH + '/' + line[4:][:-1]]
                    else:
                        nested[currPathStrH] = [currPathStrH + line[4:][:-1]]
            else:
                if len(currPath) > 1:
                    currPathStr = '/'.join(currPath)[1:]
                else:
                    currPathStr = '/'
                newLine = line.split(' ')
                dirs[currPathStr] += int(newLine[0])

    numLevels = len(levels)
    for i in range(numLevels-1, 0, -1):
        for d in levels[i]:
            size = dirs[d]
            for dUp in levels[i-1]:
                if dUp in nested and d in nested[dUp]:
                    dirs[dUp] += size
                    break

    # for part 1:   
    # res = 0
    # for dir in dirs:
    #     if dirs[dir] <= 100000:
    #         res += dirs[dir]
    # print(res)

    # for part 2:

    availableSpace = 70000000 - dirs['/']
    threshold = 30000000 - availableSpace
    comps = []
    for di in dirs:
        if dirs[di] >= threshold:
            comps.append((dirs[di], di))
    res = (float('inf'), None)
    res = min(comps)
    print(res[0])


if __name__ == '__main__':
    part1()