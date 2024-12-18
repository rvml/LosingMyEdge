from collections import defaultdict
from functools import cmp_to_key

class Solution():
    def __init__(self):
        self.rules = defaultdict(set)
        self.updates = []

    def readInput(self, filename):
        self.rules = defaultdict(set)
        self.updates = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if ('|') in line:
                    pg1, pg2 = line.split('|')
                    pg1 = pg1.strip()
                    pg2 = pg2.strip()
                    # for each page, creates a list of pages that it should be before 
                    self.rules[int(pg1)].add(int(pg2))
                elif line:
                    pages = line.split(',')
                    update = [int(pg) for pg in pages] 
                    self.updates.append(update.copy())

    def process(self, filename):
        self.readInput(filename)
        total_sum = 0
        for update in self.updates:
            sorted_update = sorted(update, key=cmp_to_key(self.compare)) 
            if sorted_update != update:
                middle = len(sorted_update)//2
                total_sum += sorted_update[middle] 
        return total_sum

    def compare(self, num1, num2):
        if num2 in self.rules[num1]: # then num1 should be in front of num2. i.e num1 is less than.
            return -1
        if num1 in self.rules[num2]: # then num 2 should be in front of num. i.e. num1 is greater than.
            return 1
        return 0 #technically I guess they're equal.

sol = Solution()
print(f"part 2 example:\t\t{sol.process('input/5/example.txt')}")
print(f"part 2 solution:\t{sol.process('input/5/input.txt')}")
