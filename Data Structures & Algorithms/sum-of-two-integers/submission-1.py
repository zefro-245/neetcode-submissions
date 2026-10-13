class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        a = a & mask
        b = b & mask

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if a >> 31:
            return a - (1 << 32)

        return a