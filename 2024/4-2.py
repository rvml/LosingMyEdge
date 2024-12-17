class Solution():
    def readInput(self, filename):
        data = []
        with open(filename, 'r') as f:
            for line in f:
                row = []
                for c in line:
                    row.append(c)
                data.append(row)
        return data

    def search(self, filename):
        data = self.readInput(filename)
        total_count = 0

        for i in range(len(data)):
            for j in range(len(data)):
                # starting at an A search for a pair of M + S diagonally left and right
                if data[i][j] == 'A':
                    # if upper left is M and lower right is S, or upper left is S and lower right is M
                    # if upper right is M and lower left is S, or upper right is S and lower left is M
                    if i <= 0 or j <= 0 or i >= len(data)-1 or j >= len(data[i])-1:
                        continue
                    upper_left = data[i-1][j-1]
                    lower_right = data[i+1][j+1]
                    if (upper_left == 'M' and lower_right == 'S') or (upper_left == 'S' and lower_right == 'M'):
                        lower_left = data[i+1][j-1]
                        upper_right = data[i-1][j+1]
                        if (lower_left == 'M' and upper_right == 'S') or (lower_left == 'S' and upper_right == 'M'):
                            total_count += 1
        return total_count

sol = Solution()
print(f"example:\t{sol.search('input/4/example2.txt')}")
print(f"solution:\t{sol.search('input/4/input.txt')}")
