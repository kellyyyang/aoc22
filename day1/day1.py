import heapq

def getCalOfEach(fileName):
    ''' input:  fileName
        output: list of calories carried by each elf
    '''
    f = open(fileName)
    lines = f.readlines()
    f.close()
    elves = []

    currCount = 0
    for line in lines:
        if line != "\n":
            currCount += int(line)
        else:
            elves.append(currCount)
            currCount = 0

    elves.append(currCount)

    return elves

def getCalOfEachHeap(fileName):
    ''' input:  fileName
        output: list of calories carried by each elf
    '''
    f = open(fileName)
    lines = f.readlines()
    f.close()
    elves = []
    heapq.heapify(elves)

    currCount = 0
    for line in lines:
        if line != "\n":
            currCount -= int(line)
        else:
            heapq.heappush(elves, currCount)
            currCount = 0

    heapq.heappush(elves, currCount)

    return elves

def part1():
    fileName = "day1_input1.txt"
    elves = getCalOfEachHeap(fileName=fileName)

    return -heapq.heappop(elves)

def part2():
    fileName = "day1_input1.txt"
    elves = getCalOfEachHeap(fileName=fileName)

    result = 0
    for i in range(3):
        result += heapq.heappop(elves)
    
    return -result

    
if __name__ == '__main__':
    print("part 1 answer:", part1())
    print("part 2 answer:", part2())