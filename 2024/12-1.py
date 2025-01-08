from collections import defaultdict
class Region():
    def __init__(self, val):
        self.val = val
        #self.plots = []
        self.area, self.perimeter = 0, 0

    def cost(self):
        return self.area * self.perimeter

class Solution():
    def __init__(self):
        self.garden_map = []
        self.width, self.height, self.total = 0, 0, 0
        self.visited = set()
        self.regions = defaultdict(list)

    def readInput(self, filename):
        self.__init__()
        with open(filename, 'r') as file:
            for line in file:
                row = []
                self.height += 1
                line = line.strip()
                if self.width == 0:
                    self.width = len(line)
                for c in line:
                    row.append(c)
                self.garden_map.append(row)

    def add(self, val1, val2):
        return (val1[0]+val2[0], val1[1]+val2[1])

    def inBounds(self, i,j):
        if i < 0 or i >= self.height or j < 0 or j >= self.width:
            return False
        return True

    def visit(self, region, i, j):
        region.area += 1
        self.visited.add((i,j))
        for (m,n) in [self.add(inc, (i,j)) for inc in [(-1,0), (1,0), (0,-1), (0,1)]]:
            #m,n = self.add(increment, (i,j))
            if not self.inBounds(m,n) or self.garden_map[m][n] != region.val:
                region.perimeter += 1
            elif (m,n) not in self.visited:
                self.visit(region, m, n)

    def getRegion(self, i, j):
        val = self.garden_map[i][j]
        region = Region(val)
        self.visit(region, i, j)
        self.regions[region.val].append(region)
        return region

    def process(self, filename):
        self.readInput(filename)
        if not self.garden_map:
            return 0
        for i in range(self.height):
            for j in range(self.width):
                if (i,j) in self.visited:
                    continue
                # every non-visited plot starts a new region
                region = self.getRegion(i,j)
                self.total += region.cost()
        return self.total
                
sol = Solution()
print(f"example:{sol.process('input/12/example.txt')}")
print(f"solution:{sol.process('input/12/input.txt')}")
