class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        n = len(intervals)
        i = 0

        while i < n:
            # Take the current interval
            current = intervals[i]
            i += 1

            # Merge all intervals that overlap with current
            while i < n and intervals[i][0] <= current[1]:
                current[1] = max(current[1], intervals[i][1])
                i += 1

            # Current is finished
            res.append(current)

        return res