class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []          # indices of increasing-height bars
        max_area = 0

        for i, h in enumerate(heights):

            # Current bar is shorter than the top bar,
            # so the top bar's right boundary has been found.
            while stack and heights[stack[-1]] > h:

                height = heights[stack.pop()]

                # Find how far this bar can extend
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, height * width)

            # Current bar hasn't found a smaller bar to its left,
            # so save its index.
            stack.append(i)

        # Remaining bars can extend to the end.
        n = len(heights)

        while stack:

            height = heights[stack.pop()]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            max_area = max(max_area, height * width)

        return max_area