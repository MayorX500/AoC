class KnotPair:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]
        self.tail_visits = {tuple([0, 0])}

    def move_head(self, direction):
        if direction == 'U':
            self.set_head([self.head[0], self.head[1] + 1])
        elif direction == 'D':
            self.set_head([self.head[0], self.head[1] - 1])
        if direction == 'L':
            self.set_head([self.head[0] - 1, self.head[1]])
        if direction == 'R':
            self.set_head([self.head[0] + 1, self.head[1]])

    def set_head(self, position):
        self.head = position
        move = [a - b for a, b in zip(self.head, self.tail)]
        if abs(move[0]) <= 1 and abs(move[1]) <= 1:
            return
        elif abs(move[0]) == 2 and abs(move[1]) == 2:
            self.tail[0] += move[0] / 2
            self.tail[1] += move[1] / 2
        elif abs(move[0]) == 2:
            self.tail[0] += move[0] / 2
            self.tail[1] = self.head[1]
        elif abs(move[1]) == 2:
            self.tail[1] += move[1] / 2
            self.tail[0] = self.head[0]
        self.tail_visits.add(tuple(self.tail))


knot_pair = KnotPair()
with open('input_file.txt', 'r') as fh:
    for row in fh:
        direction, count = row.rstrip().split(' ')
        for x in range(int(count)):
            knot_pair.move_head(direction)

print(len(knot_pair.tail_visits))

rope = [KnotPair() for x in range(9)]
with open('input_file.txt', 'r') as fh:
    for row in fh:
        direction, count = row.rstrip().split(' ')
        for x in range(int(count)):
            rope[0].move_head(direction)
            for y in range(8):
                rope[y+1].set_head(rope[y].tail)

print(len(rope[8].tail_visits))
