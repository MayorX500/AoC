#!/usr/bin/env python3

from __future__ import annotations
from enum import Enum
from queue import Queue
import time
import os

cycles_needed = [20,60,100,140,180,220]

class CPU:
    """ CPU class """
    X: int # Sprite location
    cycle: int # Cycle Counter
    display: Display # Display

    def __init__(self):
        """ Constructor """
        self.X = 1
        self.cycle = 1
        self.display = Display()

    def __repr__(self):
        """ String representation """
        return f"CPU({self.X}, {self.cycle})"

    def do_operation(self,operation: Operation):
        """ Do an operation

        Args:
        @param operation:(Operation) Operation to do

        """
        self.X += operation.value if isinstance(operation.value, int) else 0

    def clock(self,draw = False):
        """ Clock the CPU

        Args:
        @param draw:(bool) Draw the display

        """
        self.cycle += 1
        self.do_operation(self.display.get_operation(self.X))
        if draw:
            self.display.draw()
        cycle = self.cycle -1
        self.cycle += 1
        self.display.draw(cycle//40,cycle%40,self.X,draw)

class Display():
    """ Display class """
    matrix: list[list[chr]]

    def __init__(self):
        """ Constructor """
        self.matrix = [[" " for _ in range(40)] for _ in range(6)]

    def __repr__(self):
        """ String representation """
        return "\n".join(["".join(row) for row in self.matrix])

    def draw(self,row,column,cursor,print_flag = False):
        """ Draw the display

        Args:
        @param row:(int) Row to draw
        @param column:(int) Column to draw
        @param cursor:(int) Cursor location
        @param print_flag:(bool) Print the display

        """
        if column in range(cursor-1,cursor+2):
            self.matrix[row][column] = "#"
        # Clearing the Screen
        if print_flag:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self)

class Operation:
    """ Operation class """
    operation: Type_Operation # Operation Type
    value: int # Value of the operation
    takes: int # Number of cycles the operation takes

    class Type_Operation(Enum):
        """ Type of operation """
        ADD = "addx" # Add X
        NOOP = "noop" # No operation
    
    def __init__(self,operation,value=None):
        """ Constructor

        Args:
        @param operation:(str) Operation to do
        @param value:(int) Value of the operation

        """
        self.operation = self.Type_Operation(operation)
        self.value = int(value) if value else None
        self.takes = 0 if self.operation == self.Type_Operation.NOOP else 1

    def __repr__(self):
        """ String representation """
        return f"Operation('{self.operation}', '{self.value if self.value else ''}', '{self.takes}')"

def load_input() -> Queue:
    """ Load the input file
    
    Returns:
    @return:(Queue) Queue of operations
    
    """
    queue = Queue()
    with open("input_file.txt") as f:
        operations = [Operation(*line.strip().split(" ")) for line in f.readlines()]
        for operation in operations:
            queue.put(operation)
        return queue


def part_1(operations:Queue) -> int:
    """ Part 1

    Args:
    @param operations:(Queue) Queue of operations

    Returns:
    @return:(int) Value of the accumulator

    """
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
    """ Part 2

    Args:
    @param operations:(Queue) Queue of operations

    Returns:
    @return:(Display) Display

    """
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
    """ Main function """
    operations_1 = load_input()
    operations_2 = load_input()
    print(part_1(operations_1))
    print(part_2(operations_2))

if __name__ == "__main__":
    main()
