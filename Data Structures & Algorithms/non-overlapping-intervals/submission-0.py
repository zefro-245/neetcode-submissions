class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed = 0
        lastend = intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0]<lastend:
                removed+=1
            else:
                lastend = intervals[i][1]

        return removed