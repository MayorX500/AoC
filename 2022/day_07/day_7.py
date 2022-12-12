from __future__ import annotations
import time

class Directory:
    parent: Directory
    name: str
    size: int
    total_size: int
    subdirs: dict
    files: dict

    def __init__(self, name: str, parent: Directory = None):
        self.name = name
        self.parent = parent
        self.subdirs = {}
        self.files = {}
        self.size = 0
        self.total_size = 0

    def __repr__(self):
        return f"Directory({self.name}, {self.size}, {self.total_size})"

    def update_total_size(self,size:int):
        directory = self
        while directory:
            directory.total_size += size
            directory = directory.parent

    def add_subdir(self, subdir):
        self.subdirs[subdir.name] = subdir

    def add_file(self, name:str, size:int):
        self.files[name] = f"{size}"
        self.size += size
        self.update_total_size(size)

    def directory_to_list(self, depth=0):
        result = []
        result.append(self)
        for subdir in self.subdirs.values():
            result.extend(subdir.directory_to_list(depth + 1))
        return result

def load_dirs():
    current_directory = Directory("ROOT")
    root = current_directory
    count = 0
    with open("input_file.txt", "r") as f:
        for line in f:
            line = line.strip().split(" ")
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        current_directory = current_directory.parent
                    else:
                        if line[2] in current_directory.subdirs.keys():
                            current_directory = current_directory.subdirs[line[2]]
                        else:
                            new_dir = Directory(line[2],current_directory)
                            current_directory.add_subdir(new_dir)
                            current_directory = new_dir

            elif line[0].isdigit():
                current_directory.add_file(line[1],int(line[0]))

            else:
                current_directory.add_subdir(Directory(line[1],current_directory))
            count += 1

    return root.subdirs["/"]

def part_1(directories:list) -> int:
    total_size = 0
    for subdir in directories:
        if subdir.total_size <= 100000:
            total_size += subdir.total_size

    return total_size

def part_2(directories:list,tree:Directory) -> int:
    used = tree.total_size
    total = 70000000
    need = 30000000
    needed_free = need - (total - used)
    best_delete = total
    delete_directory = None
    for subdir in directories:
        if subdir.total_size >= needed_free:
            if subdir.total_size < best_delete:
                best_delete = subdir.total_size
                delete_directory = subdir

    return delete_directory.total_size

def main():
    root = load_dirs()
    directory = root.directory_to_list()
    print(part_1(directory))
    print(part_2(directory,root))

if __name__ == "__main__":
    main()
