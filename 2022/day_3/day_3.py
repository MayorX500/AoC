import string
CODE = {c: i for i,c in enumerate(string.ascii_lowercase, 1)}
CODE.update({c: i for i,c in enumerate(string.ascii_uppercase, 27)})

class Rucksack:
    full:str
    sideA:str
    sideB:str
    repeated:list

    def __init__(self, string:str):
        self.full = string
        sideA = string[:len(string)//2]
        sideB = string[len(string)//2:]
        self.sideA = sideA
        self.sideB = sideB
        self.repeated = [] # list of repeated letters
        for letter in sideA:
            if letter in sideB and letter not in self.repeated:
                self.repeated.append(letter)
        self.repeated = [CODE[letter] for letter in self.repeated]


def load_data() -> list:
    rucksacks = []
    file = open("input_file.txt", "r")
    for line in file:
        rucksacks.append(Rucksack(line.strip()))
    return rucksacks

def splitter(chunk_size:int, listed_stuff:list):
    "splitter(3, 'ABCDEFG')--> ABC DEF G"
    chunked_list = []
    for i in range(0, len(listed_stuff), chunk_size):
        chunked_list.append(listed_stuff[i:i+chunk_size])
    return chunked_list


def part_1(rucksacks:list) -> int:
    repeated_sum = 0
    for rucksack in rucksacks:
        repeated_sum += sum(rucksack.repeated)
    return repeated_sum

def part_2(rucksacks:list) -> int:
    rucksacks = splitter(3, rucksacks)
    rucksack_triplets = []
    for triple in rucksacks:
        triplelist = []
        for letter in triple[0].full:
            if letter in triple[1].full and letter in triple[2].full and letter not in triplelist:
                triplelist.append(letter)
        rucksack_triplets += [CODE[letter] for letter in triplelist]
    return sum(rucksack_triplets)


def main():
    rucksacks = load_data()
    print(part_1(rucksacks))
    print(part_2(rucksacks))


if __name__ == '__main__':
    main()
