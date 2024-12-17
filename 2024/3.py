import re

class Solution():
    def __init__(self):
        self.regex_with_instructions = "mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
        self.regex_without_instructions = "mul\([0-9]{1,3},[0-9]{1,3}\)"

    def processFile(self, filename, with_instructions):
        total_sum = 0
        enabled = True
        with open(filename, 'r') as file:
            data = file.read()
            (total_sum, enabled) = self.processData(data, with_instructions, enabled)
        return total_sum

    def processData(self, data, with_instructions, most_recent_enabled):
        total_sum = 0
        enabled = most_recent_enabled
        regex = self.regex_with_instructions if with_instructions else self.regex_without_instructions
        m = re.findall(regex, data)
        for val in m:
            if (enabled or not with_instructions) and ("mul" in val):
                total_sum += self.getProduct(val)
            if with_instructions:
                if 'don' in val:
                    enabled = False
                elif 'do(' in val:
                    enabled = True
        return (total_sum, enabled)

    def getProduct(self, val):
        val = val.strip()
        val = val[4:-1]
        num1, num2  = val.split(',')
        num1 = num1.strip()
        num2 = num2.strip()
        return int(num1) * int(num2)

sol = Solution()
print(f"example sum:\t\t\t{sol.processFile('input/3/examplePart1.txt', False)}")
print(f"example sum with instructions:\t{sol.processFile('input/3/examplePart2.txt', True)}")

print(f"sum:\t\t\t\t{sol.processFile('input/3/input.txt', False)}")
print(f"sum with instructions:\t\t{sol.processFile('input/3/input.txt', True)}")
