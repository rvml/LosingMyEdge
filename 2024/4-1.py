class Solution(): 
    def readInput(self, filename):
        data = []
        with open(filename, 'r') as f:
            for line in f:
                row = []
                for c in line:
                    row.append(c)
                data.append(row)
        return(data)

    def search(self, filename): # returns count
        data = self.readInput(filename)
        word = 'XMAS'
        total_count = 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                k = 0
                m = i
                while m >= 0 and data[m][j] == word[k]:   # search left horizontally
                    k += 1
                    m -= 1
                    if k == 4:
                        total_count += 1
                        break

                k = 0
                m = i
                while m < len(data) and data[m][j] == word[k]: # search right horizontally
                    k += 1
                    m += 1
                    if k == 4:
                        total_count += 1 
                        break

                k = 0
                m = j 
                while m >= 0 and data[i][m] == word[k]: # search up vertically
                    k += 1
                    m -= 1
                    if k == 4:
                        total_count += 1
                        break

                k = 0
                m = j
                while m < len(data[i]) and data[i][m] == word[k]: # search down vertically
                    k += 1
                    m += 1
                    if k == 4:
                        total_count += 1
                        break
 
                k = 0
                m = i
                n = j
                while m >= 0 and n >= 0 and data[m][n] == word[k]: # search diagonally upper left
                    k += 1
                    m -= 1
                    n -= 1
                    if k == 4:
                        total_count += 1
                        break

                k = 0
                m = i
                n = j
                while m >= 0 and n < len(data[m]) and data[m][n] == word[k]: # search diagonally upper right
                    k += 1
                    m -= 1
                    n += 1
                    if k == 4:
                        total_count += 1
                        break

                k = 0
                m = i 
                n = j
                while m < len(data) and n >= 0 and data[m][n] == word[k]: # search diagonally lower left
                    k += 1
                    m += 1
                    n -= 1
                    if k == 4:
                        total_count += 1
                        break

                k = 0
                m = i
                n = j
                while m < len(data) and n < len(data[m]) and data[m][n] == word[k]: # search diagonally lower right
                    k += 1
                    m += 1
                    n += 1
                    if k == 4:
                        total_count += 1
                        break

        return total_count

sol = Solution()
print(f"example:\t{sol.search('input/4/example1.txt')}")
print(f"solution:\t{sol.search('input/4/input.txt')}")
