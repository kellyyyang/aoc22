INPUT_FILE = "input.txt"

def part1():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    res = 0
    visited = set()

    # horizontal
    for ind in range(1, len(lines)-1):
        line = lines[ind].strip('\n')
        start, end = line[0], line[-1]
        line = line.strip('\n')[1:-1]
        
        maxLeft = int(start)
        maxRight = int(end)
        for i in range(len(line)):
            if int(line[i]) > maxLeft and (ind, i+1) not in visited:
                res += 1
                maxLeft = int(line[i])
                visited.add((ind, i+1))
            if int(line[len(line) - i - 1]) > maxRight and (ind, len(line) - i) not in visited:
                res += 1
                maxRight = int(line[len(line) - i - 1])
                visited.add((ind, len(line) - i))
            maxLeft = max(maxLeft, int(line[i]))
            maxRight = max(maxRight, int(line[len(line) - i - 1]))

    # vertical
    for vInd in range(1, len(lines[0]) - 2):
        vLine = [int(lines[j][vInd]) for j in range(len(lines))]
        maxTop, maxBot = vLine[0], vLine[-1]
        vLine = vLine[1:-1]
        
        for k in range(len(vLine)):
            if vLine[k] > maxTop and (k+1, vInd) not in visited:
                res += 1
                maxTop = vLine[k]
                visited.add((k+1, vInd))
            if vLine[len(vLine) - k - 1] > maxBot and (len(vLine) - k, vInd) not in visited:
                res += 1
                maxBot = vLine[len(vLine) - k - 1]
                visited.add((len(vLine) - k, vInd))
            maxTop = max(maxTop, vLine[k])
            maxBot = max(maxBot, vLine[len(vLine) - k - 1])

    print(res + 2*len(lines) + 2*(len(lines[0])-3))

def part2():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    def get_scenic_score(i, j):
        curr_height = int(lines[i][j])
        if i == 0 or j == 0 or i == len(lines) - 1 or j == len(lines[0]) - 2:
            return (curr_height, 0, 0, 0, 0,)

        # get left
        left = 0
        for a in range(j-1, -1, -1):
            if int(lines[i][a]) < curr_height:
                left += 1
            else:
                left += 1
                break

        # get right
        right = 0
        for b in range(j+1, len(lines[0])-1):
            if int(lines[i][b]) < curr_height:
                right += 1
            else:
                right += 1
                break

        # get up
        up = 0
        for c in range(i-1, -1, -1):
            if int(lines[c][j]) < curr_height:
                up += 1
            else:
                up += 1
                break

        # get down
        down = 0
        for d in range(i+1, len(lines)):
            if int(lines[d][j]) < curr_height:
                down += 1
            else:
                down += 1
                break
        
        return (curr_height, left, right, up, down)

    curr_max = -float('inf')

    for i in range(len(lines)):
        for j in range(len(lines[0])-1):
            curr_h, left, right, up, down = get_scenic_score(i, j)
            scenic_score = left * right * up * down
            curr_max = max(curr_max, scenic_score)

    print(curr_max)

if __name__ == '__main__':
    part2()