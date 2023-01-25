#!/usr/bin/env python3

import random

class Worker:
    worker_id: int
    sections:list

    def __init__(self, sections:str):
        self.worker_id = random.randint(0, 10_000_000)
        sections = sections.split("-")
        self.sections = [*range(int(sections[0]), int(sections[1]) + 1)]

    def __repr__(self):
        return f"(Worker('{str(self.sections)}'))"

    def __ne__(self, o):
        return not self.__eq__(o)

    def __eq__(self, o):
        return self.worker_id == o.worker_id

    def __contains__(self, item):
        return all(x in self.sections for x in item)

class Pair:
    worker_1:Worker
    worker_2:Worker

    def __init__(self, worker_1:Worker, worker_2:Worker):
        self.worker_1 = worker_1
        self.worker_2 = worker_2

    def __repr__(self):
        return f"(Pair({self.worker_1}, {self.worker_2}))"


def load_data() -> list:
    pairs = []
    with open("input_file.txt", "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            worker_1 = Worker(line[0])
            worker_2 = Worker(line[1])
            pairs.append(Pair(worker_1, worker_2))
    return pairs


def part_1(pairs:list) -> int:
    count = 0
    for pair in pairs:
        if pair.worker_1.sections in pair.worker_2:
            count += 1
        elif pair.worker_2.sections in pair.worker_1:
            count += 1
    return count

def part_2(pairs:list) -> int:
    count = 0
    for pair in pairs:
        for letter in pair.worker_1.sections:
            if letter in pair.worker_2.sections:
                count += 1
                break
    return count

def main():
    pairs = load_data()
    print(part_1(pairs))
    print(part_2(pairs))

if __name__ == "__main__":
    main()
