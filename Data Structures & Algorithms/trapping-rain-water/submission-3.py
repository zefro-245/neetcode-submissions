class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxl = 0
        maxr = 0
        tot = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] >= maxl:
                    maxl = height[l]
                else:
                    tot += maxl - height[l]
                l += 1

            else:
                if height[r] >= maxr:
                    maxr = height[r]
                else:
                    tot += maxr - height[r]
                r -= 1

        return tot