from __future__ import annotations
from enum import Enum
from queue import Queue
import time
import os

cycles_needed = [20,60,100,140,180,220]

class CPU:
    X: int
    cycle: int
    display: Display

    def __init__(self):
        self.X = 1
        self.cycle = 1
        self.display = Display()

    def __repr__(self):
        return f"CPU({self.X}, {self.cycle})"

    def do_operation(self,operation: Operation):
        self.X += operation.value if isinstance(operation.value, int) else 0

    def clock(self,draw = False):
        cycle = self.cycle -1
        self.cycle += 1
        self.display.draw(cycle//40,cycle%40,self.X,draw)

class Display():
    matrix: list[list[chr]]
    def __init__(self):
        self.matrix = [[" " for _ in range(40)] for _ in range(6)]

    def __repr__(self):
        return "\n".join(["".join(row) for row in self.matrix])

    def draw(self,rows,column,cursor,print_flag = False):
        if column in range(cursor-1,cursor+2):
            self.matrix[rows][column] = "#"
        # Clearing the Screen
        if print_flag:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self)

class Operation:
    operation: Type_Operation
    value: int
    takes: int

    class Type_Operation(Enum):
        ADD = "addx"
        NOOP = "noop"
    
    def __init__(self,operation,value=None):
        self.operation = self.Type_Operation(operation)
        self.value = int(value) if value else None
        self.takes = 0 if self.operation == self.Type_Operation.NOOP else 1

    def __repr__(self):
        return f"Operation('{self.operation}', '{self.value if self.value else ''}', '{self.takes}')"

def load_input() -> Queue:
    queue = Queue()
    with open("input_file.txt") as f:
        operations = [Operation(*line.strip().split(" ")) for line in f.readlines()]
        for operation in operations:
            queue.put(operation)
        return queue


def part_1(operations:Queue) -> int:
    cycle_status = {}
    cpu = CPU()
    strength = 0
    while not operations.empty():
        operation = operations.get()
        wait = operation.takes
        while wait > 0:
            cpu.clock()
            wait -= 1
            if cpu.cycle in cycles_needed:
                cycle_status[cpu.cycle] = cpu.X
        cpu.clock()
        cpu.do_operation(operation)
        if cpu.cycle in cycles_needed:
            cycle_status[cpu.cycle] = cpu.X

    for cycle,x in cycle_status.items():
        strength += x * cycle
    return strength 


def part_2(operations:Queue) -> Display:
    cpu = CPU()
    print_flag = False
    while not operations.empty():
        operation = operations.get()
        wait = operation.takes
        while wait > 0:
            cpu.clock(print_flag)
            wait -= 1
        cpu.clock(print_flag)
        cpu.do_operation(operation)
    return (cpu.display)

def main():
    operations_1 = load_input()
    operations_2 = load_input()
    print(part_1(operations_1))
    print(part_2(operations_2))

if __name__ == "__main__":
    main()
