"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)

        import heapq
        minheap=[]
        for i in range(len(intervals)):
            if minheap and intervals[i].start>=minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, intervals[i].end)

        return len(minheap)