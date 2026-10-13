class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r = len(heights)-1
        maxamt = 0
        while l<r:
            amt = min(heights[l],heights[r])*(r-l)
            maxamt = max(maxamt,amt)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxamt