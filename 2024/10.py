from collections import defaultdict

class Solution():
    def __init__(self):
        self.data = []
        self.scores = defaultdict(set)
        self.rows, self.cols, self.ratings = 0, 0, 0

    def readInput(self, filename):
        self.__init__()
        with open(filename, 'r') as file:
            for line in file:
                self.rows += 1
                row = []
                line = line.strip()
                if self.cols == 0:
                    self.cols = len(line)
                for c in line:
                    row.append(int(c))
                self.data.append(row)

    def inBounds(self, i, j):
        return i >= 0 and i < self.rows and j >= 0 and j < self.cols

    # return true if going from pos1 -> pos2 increases elevation by 1
    def isOneStep(self, pos1, pos2):
        if not self.inBounds(pos1[0], pos1[1]) or not self.inBounds(pos2[0], pos2[1]):
            return False
        level1 = self.data[pos1[0]][pos1[1]]
        level2 = self.data[pos2[0]][pos2[1]]
        return level2-level1 == 1

    def follow(self, trailhead, path):
        if len(path) == 10:
            self.scores[trailhead].add(path[-1])
            self.ratings += 1
            return
        
        i,j = path[-1]
        # check up, down, left, right
        for pos in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            if self.isOneStep((i,j),pos):
                path.append(pos)
                self.follow(trailhead, path)
                path.pop()

    def process(self, filename):
        self.readInput(filename)
        for i in range(self.rows):
            for j in range(self.cols):
                if (self.data[i][j]) == 0:
                    path = [(i,j)]
                    self.follow((i,j), path)
        total_score = 0
        for trailhead, trails in self.scores.items():
            total_score += len(trails)
        return total_score, self.ratings
       
sol = Solution()
score, ratings = sol.process('input/10/example.txt')
print(f"example score: {score}, ratings: {ratings}")
score, ratings = sol.process('input/10/input.txt')
print(f"solution score: {score}, ratings: {ratings}")
