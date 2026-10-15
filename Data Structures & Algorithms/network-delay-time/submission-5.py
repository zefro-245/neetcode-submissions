class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        graph = defaultdict(list)
        for a,b,time in times:
            graph[a].append((time,b))
        
        minheap = [(0,k)]
        mintimes = {}

        while minheap:
            curr_time, curr_src = heapq.heappop(minheap)
            if curr_src in mintimes:
                continue
            mintimes[curr_src] = curr_time

            for nei_time,nei_src in graph[curr_src]:
                tot_time = nei_time+curr_time
                if nei_src not in mintimes:
                    heapq.heappush(minheap, (tot_time, nei_src))
        if len(mintimes)!=n:
            return -1
        return max(mintimes.values())
                