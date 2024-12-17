from collections import defaultdict

class Solution():
    def __init__(self):
        self.rightlist = []
        self.leftlist = []

    def readInput(self, filename):
       with open(filename, 'r') as file:
            for line in file:
                left,right = line.split()
                left = left.strip()
                right = right.strip()
                self.leftlist.append(int(left))
                self.rightlist.append(int(right))

    def getDifferences(self):
        self.rightlist.sort()
        self.leftlist.sort()
        sum = 0
        if len(self.rightlist) != len(self.leftlist):
            raise Exception("not equal lengths")
        for i, right in enumerate(self.rightlist):
            left = self.leftlist[i] 
            sum += abs(left-right) 
        return sum

    def getOccurrences(self, locations):
        occurrences = defaultdict(int)
        for location in locations:
            occurrences[location] = occurrences[location] + 1 
        return occurrences

    def getSimilarityScore(self):
        occurrences = self.getOccurrences(self.rightlist)
        score = 0
        for location in self.leftlist:
            score += (location * occurrences[location])
        return score

sol = Solution()
sol.readInput('input/1/input.txt')
print(f"differences:\t\t{sol.getDifferences()}")
print(f"similarity score:\t{sol.getSimilarityScore()}")
