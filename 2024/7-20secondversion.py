import itertools
from collections import deque
class Solution():
    def __init__(self):
        self.data = []
        self.operators = {}

    def readInput(self, filename):
        self.__init__()
        with open(filename, 'r') as file:
            for line in file:
                left, right = line.split(':')
                result = int(left.strip())
                operands = [item.strip() for item in right.split()]
                self.data.append((result, operands))

    def calculate(self, nums_list, operators_list):
        if len(nums_list) - len(operators_list) != 1:
            raise Exception("nums is not 1 longer than operators")
        nums = deque(nums_list)
        for operator in operators_list:
            if operator == '+':
                nums.appendleft(str(int(nums.popleft()) + int(nums.popleft())))
            if operator == '*':
                nums.appendleft(str(int(nums.popleft()) * int(nums.popleft())))
            if operator == '|':
                num1 = nums.popleft()
                num2 = nums.popleft()
                nums.appendleft(num1+num2)
        return int(nums[-1])

    def process(self, filename, part2):
        operators_to_use = ['+','*']
        if part2:
            operators_to_use.append('|')
        self.readInput(filename)
        total_sum = 0
        for result, operands in self.data:
            for operators_list in itertools.product(operators_to_use, repeat=len(operands)-1):
                answer = self.calculate(operands, operators_list)
                if answer == result:
                    total_sum += result
                    break
        return total_sum 

sol = Solution()
print(f"part 1 example:\t\t{sol.process('input/7/example.txt', False)}")
print(f"part 1 solution:\t{sol.process('input/7/input.txt', False)}")
print(f"part 2 example:\t\t{sol.process('input/7/example.txt', True)}")
print(f"part 2 solution:\t{sol.process('input/7/input.txt', True)}")
