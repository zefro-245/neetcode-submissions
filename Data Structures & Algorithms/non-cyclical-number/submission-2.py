class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            sum = 0
            n = str(n)
            for i in n:
                sum += int(i)**2
            n = sum
            if sum == 1:
                return True
            if sum in seen:
                return False
            seen.add(sum)