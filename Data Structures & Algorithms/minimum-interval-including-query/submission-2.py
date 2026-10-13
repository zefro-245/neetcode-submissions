class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        import heapq
        intervals.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        res = [-1] * len(queries)
        minheap = []
        j = 0
        
        for query, original_index in sorted_queries:
            while j<len(intervals) and intervals[j][0]<=query:
                heapq.heappush(minheap,(intervals[j][1]-intervals[j][0]+1,intervals[j][1]))
                j+=1
            while minheap and minheap[0][1]<query:
                heapq.heappop(minheap)
            if minheap:
                res[original_index] = minheap[0][0]
            else:
                res[original_index] = -1
        return res
                

