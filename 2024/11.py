class Solution():
    def readInput(self, filename):
        nums = []
        with open(filename, 'r') as file:
            for line in file:
                nums += [int(val.strip()) for val in line.split()]
        return nums

    def run(self, nums, iterations):
        def blink(num, iterations):
            nonlocal mem
            if iterations == 0:
                return 1 
            if (num, iterations) in mem:
                return mem[(num, iterations)]
            res = 0
            if num == 0:
                res = blink(1, iterations-1)
            elif len(str(num)) % 2 == 0:
                strval = str(num)
                mid = len(strval)//2
                res = blink(int(strval[:mid]), iterations-1) + blink(int(strval[mid:]), iterations-1)
            else:
                res = blink(num*2024, iterations-1)
            mem[(num, iterations)] = res
            return res
        mem = {}
        count = 0
        for num in nums:
            count += blink(num, iterations)
        return count

    def process(self, filename, iterations):
        return self.run(self.readInput(filename), iterations)

sol = Solution()
print(f"example:{sol.process('input/11/example.txt', 25)}")
print(f"part 1:\t{sol.process('input/11/input.txt', 25)}")
print(f"part 2:\t{sol.process('input/11/input.txt', 75)}")
