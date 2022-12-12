from __future__ import annotations
import math
from queue import Queue

class Monkey:
    items: Queue[int]
    comparations: int
    interest_multiplier: int
    bored_multiplier: int
    test: str
    throw_success: int
    throw_fail: int

    def __init__(self, items: list[int], comparations: int,interest_multiplier: int, bored_multiplier: int, test: int, throw_success: int, throw_fail: int):
        self.items = Queue()
        for item in items:
            self.items.put(item)
        self.comparations = comparations
        self.interest_multiplier = interest_multiplier
        self.bored_multiplier = bored_multiplier
        self.test = test
        self.throw_success = throw_success
        self.throw_fail = throw_fail

    def __repr__(self):
        return f"Monkey({self.items}, {self.comparations}, {self.bored_multiplier}, {self.test})"

    def __eq__(self, other: Monkey):
        return self.items == other.items and self.comparations == other.comparations and self.bored_multiplier == other.bored_multiplier and self.test == other.test

    def __ne__(self, other: Monkey):
        return not self.__eq__(other)

    def throw_item(self,item: int,monkey: Monkey):
        monkey.items.put(item)

    def inspect_item(self) -> int:
        item = self.items.get()
        item = item * self.interest_multiplier
        item = math.floor(item/self.bored_multiplier)
        return item

    def test_item(self,item: int) -> bool:
        return item % self.test == 0

    def run(self,monkeys: dict[int,Monkey]):
        while not self.items.empty():
            item = self.inspect_item()
            if self.test_item(item):
                self.throw_item(item, monkeys[self.throw_success])
            else:
                self.throw_item(item, monkeys[self.throw_fail])


class Group:
    monkeys: dict[int, Monkey]
    _round: int

    def __init__(self, monkeys: list[Monkey]):
        self.monkeys = {}
        for monkey in monkeys:
            self.monkeys[monkey.comparations] = monkey
        self._round = 1

    def __repr__(self):
        return f"Group({self.monkeys}, {self._round})"

    def play(self):
        for i in range(len(self.monkeys.items())):
            monkey = self.monkeys[i]
            monkey.run(self.monkeys)

def load_monkeys() -> dict[int,Monkey]:
    with open("input_file.txt") as f:
        monkey_number = 0
        for line in f:
            line = line.strip()
            if line.startswith("Monkey"):
                monkey_number = line.split(" ")[1]
            else:
                option = line.strip().split(":")[0].strip()
                if option == "Starting Items":
                    list_items = string.strip().split(":")[1].strip().split(",")
                elif option == "Operation":





def main():
    monkeys = load_monkeys()

if __name__ == "__main__":
    main()
