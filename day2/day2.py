INPUT_FILE = "day2_input.txt"

RPS_DICT = {'X': 1, 'Y': 2, 'Z': 3}

# for part 1
WIN_DICT = {'A': 'Y', 'B': 'Z', 'C': 'X'} # i win
LOSE_DICT = {'A': 'Z', 'B': 'X', 'C': 'Y'} # i lose
DRAW_DICT = {'A': 'X', 'B': 'Y', 'C': 'Z'} # i draw

def part1():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    totalScore = 0

    for line in lines:
        strategy = line.split()
        totalScore += getScore(strategy[0], strategy[1])

    return totalScore

def getScore(opponent, me):
    ''' inputs: opponent, a string indicating the opponent's choice of ABC
                me, a string indicating my choice of XYZ
        output: the number of points based on the winner
    '''
    # check if win
    if me == WIN_DICT[opponent]:
        return RPS_DICT[me] + 6
    elif me == DRAW_DICT[opponent]:
        return RPS_DICT[me] + 3
    else:
        return RPS_DICT[me]

def getStrategyScore(opponent, res):
    ''' inputs: opponent, a string indicating the opponent's choice of ABC
                res, a string indicating if I should lose, draw, or win
        output: the number of points based on the winner
    '''
    # lose
    if res == 'X':
        myPoint = RPS_DICT[LOSE_DICT[opponent]]
        return myPoint
    # draw
    elif res == 'Y':
        myPoint = RPS_DICT[DRAW_DICT[opponent]]
        return myPoint + 3
    # win
    else:
        myPoint = RPS_DICT[WIN_DICT[opponent]]
        return myPoint + 6

def part2():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    totalScore = 0

    for line in lines:
        strategy = line.split()
        totalScore += getStrategyScore(strategy[0], strategy[1])

    return totalScore

if __name__ == '__main__':
    print("part 1 answer:", part1())
    print("part 2 answer:", part2())
