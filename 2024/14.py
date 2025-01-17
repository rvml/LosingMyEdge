import sys

class Solution():
    def __init__(self, filename, width, height):
        self.data, self.velocities = [], []
        self.width = width
        self.height = height
        self.readFile(filename)

    def parse(self, line):
        p = line.split(',')
        x = int(p[0][2:])
        y = int(p[1])
        return (x,y)

    def readFile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split(' ')
                (x,y) = self.parse(parts[0])
                (vx,vy) = self.parse(parts[1])
                self.data.append((x,y))
                self.velocities.append((vx,vy))

    def splitToQuadrants(self, data):
        mx = self.width//2
        my = self.height//2
        quadrants = [0]*5
        for (x,y) in data:
            if (self.width%2 == 1 and x == mx) or (self.height%2 == 1 and y == my):
                quadrants[0] += 1
            elif x < mx:
                if y < my:
                    quadrants[1] += 1   # upper left
                else:
                    quadrants[4] += 1   # lower left
            elif y < my:
                quadrants[2] += 1       # upper right
            else:
                quadrants[3] += 1       # lower right
        return quadrants

    def transformOne(self, coord, vel, time, limit):
        if time == 0:
            return coord
        diff = abs(vel * time) % limit
        if vel < 0:
            return (coord - diff) % limit
        return (coord + diff) % limit

    def transform(self, time):
        result = []
        for i,(x,y) in enumerate(self.data):
            (vx,vy) = self.velocities[i]
            nx = self.transformOne(x, vx, time, self.width)
            ny = self.transformOne(y, vy, time, self.height)
            result.append((nx,ny))
        return result

    def getSafetyFactor(self, quadrants):
        return (quadrants[1]*quadrants[2]*quadrants[3]*quadrants[4])

    def part1(self):
        snapshot = self.transform(100)
        quadrants = self.splitToQuadrants(snapshot)
        return self.getSafetyFactor(quadrants)

    def part2(self):
        t = 1 
        result = None
        minsf = sys.maxsize
        while True:
            snapshot = self.transform(t)
            quadrants = self.splitToQuadrants(snapshot)
            sf = self.getSafetyFactor(quadrants)
            if sf < minsf:
                minsf = sf
                result = t
            if t > 10000:
                break
            t += 1
        return result 

sol = Solution("input/14/example.txt", 11, 7)
print("example part 1: ", sol.part1())

sol = Solution("input/14/input.txt", 101, 103)
print("solution part1: ", sol.part1())
print("solution part2: ", sol.part2())
