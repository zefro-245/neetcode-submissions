class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = left + (right-left)//2
            time = 0
            for i in piles:
                time += math.ceil(i/mid) 
            if time <= h:
                right = mid -1
            else:
                left = mid + 1
        return left

