class Solution():
    def evaluate(self, filename, with_tolerance):
        safecount = 0
        with open(filename, 'r') as file:
            for line in file:
                if self.isSafe(line.split(), with_tolerance):
                    safecount += 1
        return safecount

    def isSafe(self, report, with_tolerance):
        isValid = self.validateReport(report)
        if isValid:
            return True
        if with_tolerance:
            for i in range(len(report)):
                newReport = self.createReportWithoutIndex(report, i)
                if self.validateReport(newReport):
                    return True
        return False

    def createReportWithoutIndex(self, report, index):
        result = []
        for i,val in enumerate(report):
            if i == index:
                continue
            result.append(val)
        return result

    def validateReport(self, report):
        if len(report) <= 1:
            return True
        first = int(report[0].strip())
        second = int(report[1].strip())
        if first == second:
            return False
        increasing = True
        if (second - first) < 0:
            increasing = False
        prev = first
        for i in range(1, len(report)):
            num = int(report[i].strip())
            if (increasing and (num < prev)) or (not increasing and (num > prev)) or abs(num-prev) < 1 or abs(num-prev) > 3:
                return False
            prev = num
        return True

sol = Solution()
print(f"safe without tolerance:\t{sol.evaluate('input/2/input.txt', False)}")
print(f"safe with tolerance:\t{sol.evaluate('input/2/input.txt', True)}")
