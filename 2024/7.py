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
        done = False

        def processOne(result, nums):
            nonlocal total_sum
            nonlocal done
            nonlocal part2
            if done:
                return

            if len(nums) == 1:
                if int(nums[0]) == result:
                    total_sum += result
                    done = True
                return

            num1 = nums.popleft()
            num2 = nums.popleft()

            #addition
            if not done:
                nums.appendleft(str(int(num1)+int(num2)))
                processOne(result, nums)
                nums.popleft()

            #multiplication
            if not done:
                nums.appendleft(str(int(num1)*int(num2)))
                processOne(result,nums)
                nums.popleft()

            #concatenation 
            if part2 and not done:
                nums.appendleft(num1+num2)
                processOne(result, nums)
                nums.popleft()

            nums.appendleft(num2)
            nums.appendleft(num1)
            return

        for result, operands in self.data: 
            done = False
            processOne(result, deque(operands)) 
        return total_sum

sol = Solution()
print(f"part 1 example:\t\t{sol.process('input/7/example.txt', False)}")
print(f"part 1 solution:\t{sol.process('input/7/input.txt', False)}")
print(f"part 2 example:\t\t{sol.process('input/7/example.txt', True)}")
print(f"part 2 solution:\t{sol.process('input/7/input.txt', True)}")
