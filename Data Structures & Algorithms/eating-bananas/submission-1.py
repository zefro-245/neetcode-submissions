class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        biggest = max(piles)

        left = 1
        right = biggest

        while left<=right:
            mid = left + (right-left)//2
            time = 0
            for i in piles:
                time+=(math.ceil(i/mid))
            if time>h:
                left = mid + 1
            elif time<=h:
                right = mid - 1
        return left
