class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxarea = 0
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                nse = i
                height = heights[stack.pop()]
                if stack:
                    pse = stack[-1]
                else:
                    pse = -1
                area = height*(nse-pse-1)
                maxarea = max(maxarea,area)
            stack.append(i)
        while stack:
            nse = n
            height = heights[stack.pop()]
            if stack:
                pse = stack[-1]
            else:
                pse = -1
            area = height*(nse-pse-1)
            maxarea = max(maxarea,area)
        return maxarea
