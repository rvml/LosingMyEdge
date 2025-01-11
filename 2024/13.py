class Solution():
    def process(self, filename, part2):
        tokens = 0
        Xa, Ya, Xb, Yb, Xp, Yp = None, None, None, None, None, None
        with open(filename, 'r') as file:
            for line in file:
                if "Button A" in line:
                    Xa,Ya = self.getXY(line)
                elif "Button B" in line:
                    Xb,Yb = self.getXY(line)
                elif "Prize" in line:
                    Xp,Yp = self.getXY(line)
                    if part2:
                        Xp += 10000000000000
                        Yp += 10000000000000
                    a = ((Xp*Yb) - (Yp*Xb)) / ((Xa*Yb) - (Ya*Xb))
                    b = ((Xp*Ya) - (Yp*Xa)) / ((Xb*Ya) - (Yb*Xa))
                    if a%1 == 0 and b%1 == 0:
                        tokens += int((a*3) + b)
        return tokens

    def getXY(self, line):
        data = line.split(':')[1]
        X, Y = data.split(',')
        X = int(X[3:].strip())
        Y = int(Y[3:].strip())
        return X, Y
              
sol = Solution()
print("example:", sol.process("input/13/example.txt", False))
print("part1:", sol.process("input/13/input.txt", False))
print("part2:", sol.process("input/13/input.txt", True))
