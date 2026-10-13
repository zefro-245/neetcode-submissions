from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        q = deque()  # stores indices

        for r in range(len(nums)):

            # Remove elements smaller than nums[r]
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Remove elements outside the window
            if q[0] < r - k + 1:
                q.popleft()

            # Window has reached size k
            if r >= k - 1:
                res.append(nums[q[0]])

        return res