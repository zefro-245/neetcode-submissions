class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            x = x * x
            n = n // 2
            return self.myPow(x, n)

        else:
            return x * self.myPow(x, n - 1)