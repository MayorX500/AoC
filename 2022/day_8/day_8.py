
def load_matrix():
    with open('input_file.txt') as f:
        return [[a for a in line.strip()] for line in f.readlines()]


def main():
    print(load_matrix())

if __name__ == '__main__':
    main()
