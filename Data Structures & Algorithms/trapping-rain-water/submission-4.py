class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftmax = height[0]
        rightmax = height[-1]
        res = 0
        while l<r:
            leftmax = max(leftmax,height[l])
            rightmax = max(rightmax,height[r])

            if leftmax<=rightmax:
                res+=max(0,leftmax-height[l])
                l+=1
            else:
                res+=max(0,rightmax-height[r])
                r-=1
        return res
            