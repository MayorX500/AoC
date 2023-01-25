#!/usr/bin/env python3

from __future__ import annotations
import enum
from copy import deepcopy
import time

class Node:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Node('{self.x}', '{self.y}')"

    def move(self, direction: Move.Direction):
        if direction == Move.Direction.UP:
            self.y += 1
        elif direction == Move.Direction.DOWN:
            self.y -= 1
        elif direction == Move.Direction.LEFT:
            self.x -= 1
        elif direction == Move.Direction.RIGHT:
            self.x += 1

    def to_list(self):
        return [self.x, self.y]

    def to_str(self):
        return f"{self.x},{self.y}"

class Rope:
    head: Node
    tail: Node
    tail_passed: dict

    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail_passed = {}

    def __repr__(self):
        return f"Rope({self.head}, {self.tail})"

    def move(self, direction: Move.Direction):
        new = deepcopy(self.head)
        new.move(direction)
        self.set_head(new)

    def set_head(self,head_: Node):
        old = deepcopy(self.head)
        self.head = head_
        self.update(old)
        self.tail_passed[self.tail.to_str()] = True

    def attached(self)-> bool:
        x = abs(self.head.x - self.tail.x)
        y = abs(self.head.y - self.tail.y)
        if x > 1 or y > 1:
            return False
        else:
            return True

    def update(self,old_pos: Node):
        if not self.attached():
            self.tail = deepcopy(old_pos)

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

def part_1(moves: list[Move]):
    rope = Rope()
    for move in moves:
        for _ in range(move.distance):
            rope.move(move.direction)
    visited = len(rope.tail_passed.keys())

    return visited

def part_2(moves: list[Move]):
    big_rope = [Rope() for _ in range(9)]
    for move in moves:
        for _ in range(move.distance):
            big_rope[0].move(move.direction)
            for i in range(8):
                big_rope[i+1].set_head(big_rope[i].tail)
    visited = len(big_rope[len(big_rope)-1].tail_passed.keys())

    return visited




def main():
    moves = load_moves()
    print(part_1(moves))
    print(part_2(moves))

if __name__ == '__main__':
    main()
