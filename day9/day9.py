INPUT_FILE = "input.txt"

def part1():
    f = open(INPUT_FILE)
    lines = f.readlines()
    f.close()

    visited = {(0, 0)} # set containing visited positions
    pos = {'R': [1, 0], 'L':[-1, 0], 'U': [0, 1], 'D': [0, -1]}

    def get_tail_pos(head, tail, move):
        # check if tail is touching head
        # same x-coordinate and directly above or below or at the same position
        if head[0] == tail[0] and (head[1] == tail[1] + 1 or head[1] == tail[1] - 1 or head[1] == tail[1]):
            return tail
        # same y-coordinate and directly to the left or right
        elif head[1] == tail[1] and (head[0] == tail[0] + 1 or head[0] == tail[0] - 1):
            return tail
        # upper adjacent diagonal
        elif (head[0] == tail[0] + 1 or head[0] == tail[0] - 1) and (head[1] == tail[1] + 1):
            return tail
        # lower adjacent diagonal
        elif (head[0] == tail[0] + 1 or head[0] == tail[0] - 1) and (head[1] == tail[1] - 1):
            return tail
        # not touching
        else:
            # same column or same row
            if head[0] == tail[0] or head[1] == tail[1]:
                tail = [tail[k] + pos[move][k] for k in range(2)]
            else:
                if head[0] > tail[0] and head[1] > tail[1]: # move must have been R or U
                    tail = [tail[i] + 1 for i in range(2)]
                elif head[0] > tail[0] and head[1] < tail[1]: # move must have been R or D
                    tail[0] += 1
                    tail[1] -= 1
                elif head[0] < tail[0] and head[1] > tail[1]: # move must have been L or U
                    tail[0] -= 1
                    tail[1] += 1
                elif head[0] < tail[0] and head[1] < tail[1]: # move must have been L or D
                    tail = [tail[i] - 1 for i in range(2)]
            return tail

    # T, H start at (0, 0)
    head, tail = [0, 0], [0, 0]
    for line in lines:
        line = line.split()
        move, num = line[0], int(line[1])
        for i in range(num):
            head = [head[j] + pos[move][j] for j in range(2)]
            new_tail = get_tail_pos(head, tail, move)
            visited.add(tuple(new_tail))
            tail = new_tail

    print(visited)
    return len(visited)

if __name__ == '__main__':
    print(part1())