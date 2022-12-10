from __future__ import annotations
import enum

class Node:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Node({self.x}, {self.y})"

    def move(self, direction: Direction):
        if direction == Direction.UP:
            self.y -= 1
        elif direction == Direction.DOWN:
            self.y += 1
        elif direction == Direction.LEFT:
            self.x -= 1
        elif direction == Direction.RIGHT:
            self.x += 1

class Rope:
    head: Node
    tail: Node

    def __init__(self, head: Node, tail: Node):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return f"Rope({self.head}, {self.tail})"

    def move(self, direction: Direction):
        self.head.move(direction)
        self.tail.update()

    def update(self):


class Map:
    rope



class Move:
    direction: Direction
    distance: int

    class Direction(enum.Enum):
        UP = 'U'
        DOWN = 'D'
        LEFT = 'L'
        RIGHT = 'R'

    def __init__(self,line):
        self.direction = self.Direction(line[0])
        self.distance = int(line[1])

    def __repr__(self):
        return f"{self.direction.name} {self.distance}"


def load_moves():
    moves_list = []
    with open('input_file.txt') as f:
        for line in f:
             moves_list.append(Move(line.strip().split(' ')))
    return moves_list

def main():
    moves = load_moves()
    print(moves)

if __name__ == '__main__':
    main()
