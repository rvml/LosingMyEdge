class Region():
    def __init__(self, val):
        self.val = val
        self.area = 0
        self.corners = 0

    def cost(self):
        return self.area * self.corners

class Solution():
    def __init__(self):
        self.garden = []
        self.visited = set()

    def readInput(self, filename, verbose):
        self.__init__()
        with open(filename, 'r') as file:
            for line in file:
                row = []
                for c in line.strip():
                    row.append(c)
                self.garden.append(row)
                if verbose:
                    print(row)

    def move(self, pos, direction):
        if direction == 'up':
            return (pos[0]-1, pos[1])
        elif direction == 'right':
            return (pos[0], pos[1]+1)
        elif direction == 'down':
            return (pos[0]+1, pos[1])
        elif direction == 'left':
            return (pos[0], pos[1]-1)
        elif direction == 'upperleft':
            return (pos[0]-1, pos[1]-1)
        elif direction == 'upperright':
            return (pos[0]-1, pos[1]+1)
        elif direction == 'lowerleft':
            return (pos[0]+1, pos[1]-1)
        elif direction == 'lowerright':
            return (pos[0]+1, pos[1]+1)
        return pos

    def isEdge(self, pos, direction):
        i,j = pos
        val = self.garden[i][j]
        i,j = self.move((i,j), direction)
        return i < 0 or i >= len(self.garden) or j < 0 or j >= len(self.garden[i]) or self.garden[i][j] != val

    def isInRegion(self, pos, direction):
        i,j = pos
        val = self.garden[i][j]
        i,j = self.move((i,j), direction)
        return i >= 0 and i < len(self.garden) and j >= 0 and j < len(self.garden[i]) and self.garden[i][j] == val

    def visit(self, pos, region):
        region.area += 1
        self.visited.add(pos)
        # need to count corners.
        for pair in [('up','left','upperleft'), ('up','right','upperright'), ('down','left','lowerleft'), ('down','right','lowerright')]:
            if (self.isEdge(pos, pair[0]) and self.isEdge(pos, pair[1])) or (self.isInRegion(pos, pair[0]) and self.isInRegion(pos, pair[1]) and not self.isInRegion(pos, pair[2])):
                region.corners += 1
        for direction in ['up', 'right', 'down', 'left']:
            if self.isInRegion(pos, direction):
                next_pos = self.move(pos, direction)
                if next_pos not in self.visited:
                    self.visit(next_pos, region)

    def process(self, filename, verbose):
        self.readInput(filename, verbose)
        total = 0
        for i in range(len(self.garden)):
            for j in range(len(self.garden[i])):
                if (i,j) not in self.visited:
                    region = Region(self.garden[i][j])
                    self.visit((i,j), region)
                    if verbose:
                        print(f"region val: {region.val} area: {region.area} corners: {region.corners}")
                    total += region.cost()
        return total

sol = Solution()
print(f"example: {sol.process('input/12/example.txt', True)}")
print(f"example: {sol.process('input/12/example2.txt', True)}")
print(f"example: {sol.process('input/12/example3.txt', True)}")
print(f"solution: {sol.process('input/12/input.txt', False)}")
