from collections import defaultdict

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
                    self.rules[int(pg2)].add(int(pg1))
                elif line:
                    pages = line.split(',')
                    update = [int(pg) for pg in pages] 
                    self.updates.append(update.copy())

    def process(self, filename):
        self.readInput(filename)
        total_sum = 0 
        for update in self.updates:
            total_sum += self.processOne(update)
        return total_sum

    def processOne(self, update):
            if len(update) == 1:
                return update[0]
            # create a sort of "suffix set" of values after the current index
            running_set = [set() for i in range(len(update))]
            s = {update[-1]}
            for i in range(len(update)-2, -1, -1):
                s.add(update[i+1])
                running_set[i] = s.copy()
            for i, pg in enumerate(update):
                rules = self.rules[pg]
                for prevpage in rules:
                    if prevpage in running_set[i]:
                        # this means that a page that should've been before it, is actually after it
                        return 0
            #this update is valid. return the middle value
            middle = len(update)//2
            return update[middle] 

sol = Solution()
print(f"part 1 example:\t\t{sol.process('input/5/example.txt')}")
print(f"part 1 solution:\t{sol.process('input/5/input.txt')}")
