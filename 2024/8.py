from collections import defaultdict
import itertools
import math

class Solution():
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.frequencies = defaultdict(set)
        self.output = []

    def readInput(self,filename):
        self.__init__()
        with open(filename, 'r') as file:
            for i,line in enumerate(file):
                row = []
                self.rows += 1
                line = line.strip()
                if self.cols == 0:
                    self.cols = len(line)
                for j,c in enumerate(line):
                    row.append(c)
                    if c == '.':
                        continue
                    self.frequencies[c].add((i,j)) 
                self.output.append(row)

    def inBounds(self, loc):
        return (loc[0] >= 0 and loc[0] < self.rows and loc[1] >= 0 and loc[1] < self.cols)

    def subtract(self, first, second):
        return (first[0]-second[0], first[1]-second[1])

    def add(self, first, second):
        return (first[0]+second[0], first[1]+second[1])

    def printMap(self):
        for row in (self.output):
            print(''.join(row))
        print('\n')

    def part1(self, filename, print_map):
        self.readInput(filename)
        if print_map:
            self.printMap()
        antinodes = set()
        for key,frequency_set in self.frequencies.items():
            for combo in itertools.combinations(frequency_set, 2):
                # distance to get from 0 to 1
                diff = self.subtract(combo[1], combo[0])
                # antinodes are at loc1+diff and loc0-diff
                a1 = self.add(combo[1], diff)
                a2 = self.subtract(combo[0], diff)
                if self.inBounds(a1):
                    antinodes.add(a1)
                if self.inBounds(a2):
                    antinodes.add(a2)
        for (i,j) in antinodes:
            self.output[i][j] = '#'
        if print_map:
            self.printMap()
        return len(antinodes)

    def part2(self, filename, print_map):
        self.readInput(filename)
        if print_map:
            self.printMap()
        antinodes = set()
        for key, frequency_set in self.frequencies.items():
            for combo in itertools.combinations(frequency_set, 2):
                antinodes.add(combo[0])
                antinodes.add(combo[1])
                diff = self.subtract(combo[1], combo[0])
                gcd = (math.gcd(diff[0], diff[1]))
                if gcd > 1:
                    diff = (diff[0]/gcd, diff[1]/gcd)
                a1 = self.add(combo[1], diff)
                while self.inBounds(a1):
                    antinodes.add(a1)
                    a1 = self.add(a1, diff)
                a2 = self.subtract(combo[0], diff)
                while self.inBounds(a2):
                    antinodes.add(a2)
                    a2 = self.subtract(a2, diff)
        for (i,j) in antinodes:
            self.output[i][j] = '#'
        if print_map:
            self.printMap()
        return len(antinodes)

sol = Solution()
print(f"part 1 example:\t{sol.part1('input/8/example.txt', False)}")
print(f"part 1 solution:{sol.part1('input/8/input.txt', False)}")
print(f"part 2 example:\t{sol.part2('input/8/example.txt', False)}")
print(f"part 2 solution:{sol.part2('input/8/input.txt', False)}")
