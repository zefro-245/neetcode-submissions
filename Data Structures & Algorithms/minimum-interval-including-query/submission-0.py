class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        import heapq

        intervals.sort()

        # Store (query, original_index)
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        res = [-1] * len(queries)

        minheap = []
        j = 0

        for query, original_index in sorted_queries:

            # Add all intervals that have started
            while j < len(intervals) and intervals[j][0] <= query:
                heapq.heappush(
                    minheap,
                    (
                        intervals[j][1] - intervals[j][0] + 1,
                        intervals[j][1]
                    )
                )
                j += 1

            # Remove intervals that have already ended
            while minheap and minheap[0][1] < query:
                heapq.heappop(minheap)

            # Smallest valid interval
            if minheap:
                res[original_index] = minheap[0][0]
            else:
                res[original_index] = -1

        return res