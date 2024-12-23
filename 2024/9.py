class Diskblock():
    def __init__(self, file_id, start, numblocks):
        self.id = file_id
        self.start = start
        self.len = numblocks

class Solution():
    def __init__(self):
        self.diskmap, self.filespaces, self.freespaces = [], [], []

    def readInput(self, filename):
        self.__init__()
        file_id, free_id = 0, 0
        with open(filename, 'r') as file:
            data = file.read()
            data = data.strip()
            for i,c in enumerate(data):
                if int(c) == 0:
                    continue
                if i % 2 == 0:
                    # files indicator
                    self.filespaces.append(Diskblock(file_id, len(self.diskmap), int(c)))
                    for k in range(int(c)):
                        self.diskmap.append(file_id)
                    file_id += 1
                else:
                    # free space indicator
                    self.freespaces.append(Diskblock(free_id, len(self.diskmap), int(c)))
                    for k in range(int(c)):
                        self.diskmap.append(None)
                    free_id += 1

    def compactData(self):
        i, j = 0, len(self.diskmap)-1
        while True:
            while self.diskmap[i] != None:
                i += 1
            while self.diskmap[j] == None:
                j -= 1
            if i > j:
                break
            self.diskmap[i] = self.diskmap[j]
            self.diskmap[j] = None

    def compactWithoutFragmentation(self):
        for j in range(len(self.filespaces)-1, -1, -1):
            filespace = self.filespaces[j]
            for freespace in self.freespaces:
                if freespace.len < filespace.len:
                    continue
                m = freespace.start
                n = filespace.start
                if m > n:
                    break
                for i in range(filespace.len):
                    self.diskmap[m+i] = self.diskmap[n+i]
                    self.diskmap[n+i] = None
                freespace.len -= filespace.len
                freespace.start += filespace.len
                filespace.start = m
                break

    def calculateChecksum(self):
        checksum = 0
        for i,val in enumerate(self.diskmap):
            if val != None:
                checksum += (i * val)
        return checksum

    def process(self, filename, part1):
        self.readInput(filename)
        self.compactData() if part1 else self.compactWithoutFragmentation()
        return self.calculateChecksum()

sol = Solution()
print(f"part 1 example:\t\t{sol.process('input/9/example.txt', True)}")
print(f"part 1 solution:\t{sol.process('input/9/input.txt', True)}")
print(f"part 2 example:\t\t{sol.process('input/9/example.txt', False)}")
print(f"part 2 solution:\t{sol.process('input/9/input.txt', False)}")
