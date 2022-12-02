INPUT_FILE = "day2_input.txt"

RPS_DICT = {'X': 1, 'Y': 2, 'Z': 3}
WIN_DICT = {'A': 'Y', 'B': 'Z', 'C': 'X'} # i win
LOSE_DICT = {'A': 'Z', 'B': 'X', 'C': 'Y'} # i lose
DRAW_DICT = {'A': 'X', 'B': 'Y', 'C': 'Z'} # i draw

def main():
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

if __name__ == '__main__':
    print(main())
