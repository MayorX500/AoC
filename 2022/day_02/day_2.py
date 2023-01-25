#!/usr/bin/env python3

Victory = {'Rock':'Scissors','Paper':'Rock','Scissors':'Paper'}
Draw = {'Rock':'Rock','Paper':'Paper','Scissors':'Scissors'}
Loss = {'Rock':'Paper','Paper':'Scissors','Scissors':'Rock'}
Points = {'Rock':1,'Paper':2,'Scissors':3}

Keys = {'A':'Rock','B':'Paper','C':'Scissors','X':'Rock','Y':'Paper','Z':'Scissors'}
Need = {'X':Victory,'Y':Draw,'Z':Loss}

class Strat:
    me:str
    need:str
    opponent:str
    outcome:int
    points:int

    def __init__(self,opponent,me):
        self.me = Keys[me] 
        self.opponent = Keys[opponent]
        self.need = Need[me]
        self.outcome = 0
        self.points = 0


    def __repr__(self):
        return f"Strat('{self.me}','{self.opponent}','{self.outcome}','{self.points}')"

    def update_points(self):
        if Victory[self.me] == self.opponent:
            self.outcome = 6
        elif Draw[self.me] == self.opponent:
            self.outcome = 3
        else:
            self.outcome = 0
        self.points = Points[self.me]

    def get_points(self) -> int:
        return self.points + self.outcome

def load_strats() -> list:
    file = open('input_file.txt','r')
    strats = []
    for line in file:
        line = line.strip()
        line = line.split(' ')
        strats.append(Strat(*line))
    return strats

def part_1(strats:list) -> int:
    points = 0
    for strat in strats:
        strat.update_points()
        points += strat.get_points()
    return points

def part_2(strats:list) -> int:
    points = 0
    for game in strats:
        game.me = game.need[game.opponent]
        game.update_points()
        points += game.get_points()
    return points

def main():
    strats = load_strats()
    print(part_1(strats))
    print(part_2(strats))

if __name__ == '__main__':
    main()
