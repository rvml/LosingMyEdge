import pprint
class Solution():
    def __init__(self):
        self.obstructions, self.unique_visited = set(), set()
        self.num_rows, self.width, self.visited_count = 0, 0, 0
        self.guard_dir, self.guard_pos, self.initial = None, None, None
        self.directions = {
            '^': 0,
            '>': 1,
            'v': 2,
            '<': 3,
        }
        self.increments = [
            (-1,0),
            (0,1),
            (1,0),
            (0,-1)
        ] 

    def readInput(self, filename):
        self.__init__()
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                self.num_rows += 1
                line = line.strip()
                if self.width == 0:
                    self.width = len(line)
                for j, c in enumerate(line):
                    if c in self.directions:
                        self.guard_dir = self.directions[c]
                        self.guard_pos = (i,j)
                        self.initial = (self.guard_pos, self.guard_dir)
                    if c == '#':
                        self.obstructions.add((i,j))

    def turn(self):
        if self.guard_dir == 3:
            self.guard_dir = 0
        else:
            self.guard_dir += 1

    def getNextPos(self):
        increment = self.increments[self.guard_dir]
        return (self.guard_pos[0]+increment[0], self.guard_pos[1]+increment[1])

    # return false if the next move is out of bounds, else return true
    def guardMove(self):
        next_pos = self.getNextPos()
        while next_pos in self.obstructions:
            self.turn()
            next_pos = self.getNextPos()
        if next_pos[0] < 0 or next_pos[0] >= self.num_rows or next_pos[1] < 0 or next_pos[1] >= self.width:
            return False
        self.guard_pos = next_pos
        return True
      
    def countPositions(self, filename): 
        self.readInput(filename)
        self.visited_count = 1 # starting position
        self.unique_visited.add(self.guard_pos)
        while True:
            if not self.guardMove():
                break
            if self.guard_pos not in self.unique_visited:
                self.visited_count += 1
            self.unique_visited.add(self.guard_pos)
        return self.visited_count

    def getNewObstructions(self, filename):
        self.countPositions(filename)
        result = 0
        #iterate only along the path the guard was already walking on
        for (i,j) in self.unique_visited:
            #can't add an obstruction where the guard starts
            if (i,j) == self.initial[0]:
                continue
            # put the guard back at the original position
            self.guard_pos = self.initial[0]
            self.guard_dir = self.initial[1]
            # add a new obstruction
            self.obstructions.add((i,j))
            new_visited = set()
            new_visited.add(self.initial)
            in_bounds = self.guardMove()
            while in_bounds:
                if (self.guard_pos, self.guard_dir) in new_visited:
                    # back to an already visted position, and headed the same direction. so there will be a loop.
                    result += 1
                    break
                new_visited.add((self.guard_pos, self.guard_dir))
                in_bounds = self.guardMove()
            self.obstructions.remove((i,j))
        return result

sol = Solution()
print(f"part 1 example:\t\t{sol.countPositions('input/6/example.txt')}")
print(f"part 1 solution:\t{sol.countPositions('input/6/input.txt')}")
print(f"part 2 example:\t\t{sol.getNewObstructions('input/6/example.txt')}")
print(f"part 2 solution:t\t{sol.getNewObstructions('input/6/input.txt')}")
