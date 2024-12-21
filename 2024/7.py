from collections import deque

class Solution():
    def __init__(self):
        self.data = []

    def readInput(self, filename):
        self.__init__()
        with open(filename, 'r') as file:
            for line in file:
                left, right = line.split(':')
                result = int(left.strip())
                operands = [item.strip() for item in right.split()]
                self.data.append((result, operands))
    
    def process(self, filename, part2):
        self.readInput(filename)
        total_sum = 0
        found = False

        def processOne(result, nums):
            nonlocal total_sum
            nonlocal found
            nonlocal part2
            if found:
                return

            if len(nums) == 1:
                if int(nums[0]) == result:
                    total_sum += result
                    found = True
                return

            num1 = nums.popleft()
            num2 = nums.popleft()

            #addition
            if not found:
                value = str(int(num1)+int(num2))
                nums.appendleft(value)
                processOne(result, nums)
                nums.popleft()

            #multiplication
            if not found:
                value = str(int(num1)*int(num2))
                nums.appendleft(value)
                processOne(result,nums)
                nums.popleft()

            #concatenation 
            if part2 and not found:
                value = num1 + num2
                nums.appendleft(value)
                done = processOne(result, nums)
                nums.popleft()

            nums.appendleft(num2)
            nums.appendleft(num1)
            return

        for result, operands in self.data: 
            nums = deque(operands)
            found = False
            processOne(result, deque(operands)) 
        return total_sum

sol = Solution()
print(f"part 1 example:\t\t{sol.process('input/7/example.txt', False)}")
print(f"part 1 solution:\t{sol.process('input/7/input.txt', False)}")
print(f"part 2 example:\t\t{sol.process('input/7/example.txt', True)}")
print(f"part 2 solution:\t{sol.process('input/7/input.txt', True)}")
