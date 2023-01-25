#!/usr/bin/env python3

import numpy

class Forest:
    """ A forest of trees """
    trees: list[list[int]] # Matrix of Trees
    visible_trees: list[list[bool]] # Matrix of visible_trees from the outside
    scenic_score: list[list[int]] # Scenic score for each tree in the forest
    width: int # Width of the forest
    height: int # Height of the forest

    def __init__(self, trees: list[list[int]]):
        """ Constructor for the Forest class

        Args:
        @param trees:list[list[int]] A matrix of trees

        """

        self.trees = trees
        self.visible_trees = [[False for _ in row] for row in trees]
        self.scenic_score = [[0 for _ in row] for row in trees]
        self.width = len(trees[0])
        self.height = len(trees)

    def __repr__(self):
        """ String representation """
        forest ="\n"+ '\n'.join("".join(a for a in row)for row in self.trees) + "\n"
        return f"Forest({forest})"

    def print_visible(self):
        """ Print the visible trees """
        return "\n".join("".join("#" if tree else " " for tree in row) for row in self.visible_trees)

    def print_scenic(self):
        """ Print the scenic score """
        print("\n".join(", ".join(str(score) for score in row) for row in self.scenic_score))


def load_matrix() -> Forest:
    """ Load the matrix from the input file """
    with open('input_file.txt') as f:
        return Forest([[a for a in line.strip()] for line in f.readlines()])



def check_visible(forest):
    """ Check which trees are visible from the outside """
    for row in range(forest.height):
        max_height = forest.trees[row][0]
        for col in range(forest.width):
            tree_height = forest.trees[row][col]
            if tree_height > max_height:
                max_height = tree_height
                forest.visible_trees[row][col] = True

    return forest

def rotate_matrix( m: list[list[int]]) -> list[list[int]]:
    """ Rotate a matrix 90 degrees clockwise

    Args:
    @param m:list[list[int]] A matrix

    Returns:
    @return list[list[int]] The rotated matrix

    """
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def transpose(forest: Forest) -> Forest:
    """ Transpose a forest

    Args:
    @param forest:Forest A forest

    Returns:
    @return Forest The transposed forest

    """
    forest.trees = rotate_matrix(forest.trees)
    forest.visible_trees = rotate_matrix(forest.visible_trees)
    forest.width = len(forest.trees[0])
    forest.height = len(forest.trees)
    return forest

def part_1(forest: Forest) -> int:
    """ Part 1 of the challenge

    Args:
    @param forest:Forest A forest

    Returns:
    @return int The number of visible trees

    """
    for tree in range(forest.width):
        forest.visible_trees[0][tree] = True
        forest.visible_trees[forest.height-1][tree] = True
        forest.visible_trees[tree][0] = True
        forest.visible_trees[tree][forest.width-1] = True
    for i in range(5):
        forest = check_visible(forest)
        forest = transpose(forest)

    count = 0
    for line in forest.visible_trees:
        for tree in line:
            if tree:
                count += 1

    return count

def part_2(forest: Forest) -> int:
    """ Part 2 of the challenge

    Args:
    @param forest:Forest A forest

    Returns:
    @return int The scenic score

    """
    for row in range(forest.height):
        for col in range(forest.width):
            tree_height = forest.trees[row][col]

            # get all trees from tree[row][col]
            left = list(reversed([x for x in forest.trees[row][:col]]))
            right = [x for x in forest.trees[row][col+1:]]
            up = list(reversed([x[col] for x in forest.trees[:row] if x[col]]))
            down = [x[col] for x in forest.trees[row+1:] if x[col]]
            scenic_map = [left, right, up, down]
            
            scenic_view = []
            for direction in scenic_map:
                distance = 0
                for distance in range(len(direction)):
                    if direction[distance] >= tree_height:
                        break
                scenic_view.append(distance+1)

            forest.scenic_score[row][col] = numpy.prod(scenic_view)

    return max(map(max, forest.scenic_score))


def main():
    forest = load_matrix()
    print(part_1(forest))
    print(part_2(forest))

if __name__ == '__main__':
    main()
