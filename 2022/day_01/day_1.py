#!/usr/bin/env python3

from __future__ import annotations

class Elf:
    def __init__(self):
        self.magical_energy = 0
        self.number_star_fruits = 0
        
    def __repr__(self) -> str:
        return f'Elf("{self.magical_energy}", "{self.number_star_fruits}")'
    
    def __str__(self) -> str:
        return f"Elf has {self.magical_energy} magical energy from {self.number_star_fruits} starfruits"
    
    def __eq__(self,other:Elf):
        return self.magical_energy == other.magical_energy
    
    def __gt__(self,other:Elf):
        return self.magical_energy > other.magical_energy
    
    def __ge__(self,other:Elf):
        return self.magical_energy >= other.magical_energy
    
    def __lt__(self,other:Elf):
        return self.magical_energy < other.magical_energy
    
    def __le__(self,other:Elf):
        return self.magical_energy <= other.magical_energy
    
    def __ne__(self,other:Elf):
        return self.magical_energy != other.magical_energy

    
    def add(self,magical_energy):
        """Add a fruit to the elf's repertoire"""
        self.magical_energy += magical_energy
        self.number_star_fruits += 1
        
        
    def get_magical_energy(self):
        """Returns elf's gathered energy"""
        return self.magical_energy    
    
    
    @staticmethod
    def max_elf(elfs:list[Elf],n = 1):
        """Return n max elfs"""
        return sorted(elfs)[-n:]


def load_elfs():
    """Load File to a list of Elfs"""
    elfs = [Elf()]
    elf_counter = 0
    
    try:
        file = open('input_file.txt','r')
        for line in file:
            if len(line) == 1:
                elfs.append(Elf())
                elf_counter += 1
            else:
                elfs[elf_counter].add(int(line))
    except:
        exit(-1)
    return elfs      

def part_1(elfs:list[Elf]) -> int:
    """Part 1 of the Challenge
    
    Returns magical energy gathered by the top elf
    """
    top_elf = Elf.max_elf(elfs)
    #print(repr(top_elf[0]))
    return top_elf[0].magical_energy      

def part_2(elfs:list[Elf]) -> int:
    """Part 2 of the Challenge
    
    Returns magical energy gathered by the top 3 elfs
    """
    top_three_elfs = Elf.max_elf(elfs,n=3)
    top_three_elfs_magical_energy = 0
    for elf in top_three_elfs:
        #print(repr(elf))
        top_three_elfs_magical_energy += elf.get_magical_energy()
    #print(top_three_elfs_magical_energy)
    return top_three_elfs_magical_energy


def main():
    elfs = load_elfs()
    print(part_1(elfs))
    print(part_2(elfs))
      

if __name__ == '__main__':
    main()
