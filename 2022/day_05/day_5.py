import queue

class Container:
    identifier:chr

    def __init__(self, identifier:chr):
        self.identifier = identifier

    def __repr__(self):
        return f"Container({self.identifier})"

    def __str__(self):
        return f"{self.identifier}"

class Move:
    from_bay:int
    to_bay:int
    containers:int

    def __init__(self, from_bay:int, to_bay:int, containers:int):
        self.from_bay = from_bay
        self.to_bay = to_bay
        self.containers = containers

    def __repr__(self):
        return f"Move({self.from_bay}, {self.to_bay}, {self.containers})"

class Container_Ship:
    bays:list[queue.Queue] = []

    def __init__(self):
        pass

    def __repr__(self):
        bays = []
        for i in range(0,len(self.bays)):
            bays.append(f"Bay_{i+1}({list(self.bays[i].queue)})")
        bays = ", ".join(bays)
        return f"Container_Ship({bays})"

    def load_bay(self, bay:int, container:Container):
        bay = bay-1 # 1-indexed because input is 1-indexed
        while bay >= len(self.bays):
            self.bays.append(queue.LifoQueue())
        self.bays[bay].put(container)

    def make_move(self, move:Move):
        from_bay = move.from_bay-1
        to_bay = move.to_bay-1
        how_many = move.containers
        while to_bay > len(self.bays):
            self.bays.append(queue.LifoQueue())
        for i in range(0,how_many):
            self.bays[to_bay].put(self.bays[from_bay].get())

    def make_moves_queued(self,move:Move):
        from_bay = move.from_bay-1
        to_bay = move.to_bay-1
        how_many = move.containers
        temporary_queue = queue.LifoQueue()
        while how_many > 0:
            temporary_queue.put(self.bays[from_bay].get())
            how_many -= 1
        how_many = move.containers
        while how_many > 0:
            self.bays[to_bay].put(temporary_queue.get())
            how_many -= 1

def load_data() -> (Container_Ship, list[Move]):
    ship = Container_Ship()
    moves = []
    with open("input_file.txt") as f:
        for line in f:
            if not line.startswith("#"):
                line = line.strip().split(" ")
                if line[0].isdigit():
                    for container in line[1:]:
                        ship.load_bay(int(line[0]), Container(container[1:-1]))
                elif line[0] == "move":
                    moves.append(Move(int(line[3]), int(line[5]), int(line[1])))
    return (ship, moves)


def part_1(ship_og:Container_Ship, moves_og:list[Move],mover=Container_Ship.make_move) -> str:
    ship = ship_og
    moves = moves_og
    for move in moves:
        mover(ship, move)
    top_containers = ""
    for bay in ship.bays:
        top_containers += str(bay.get())
    return top_containers

def part_2(ship_og:Container_Ship, moves:list[Move]) -> str:
    return part_1(ship_og, moves, mover=Container_Ship.make_moves_queued)


def main():
    ship, moves = load_data()
    print(part_1(ship, moves))
    ship, moves = load_data()
    print(part_2(ship, moves))


if __name__ == "__main__":
    main()
