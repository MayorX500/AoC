#!/usr/bin/env python3



def load_input():
    with open('input_file.txt') as f:
        return f.read().strip()


def check_markers(input_stream:str,size:int):
    start = 0
    stop = size
    found = False
    while not found:
        signal = input_stream[start:stop:1]
        letter_list = [letter for letter in signal]
        for letter in signal:
            if signal.count(letter) > 1:
                letter_list.remove(letter)

        if len(letter_list) == size:
            found = True
        else:
            start += 1
            stop += 1
    return stop

def part_1(input_stream:str):
    return check_markers(input_stream,4)

def part_2(input_stream:str):
    return check_markers(input_stream,14)

def main():
    input_stream = load_input()
    print(part_1(input_stream))
    print(part_2(input_stream))

if __name__ == "__main__":
    main()
