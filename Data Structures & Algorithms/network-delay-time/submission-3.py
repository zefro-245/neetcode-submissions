class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        adjlist = [[] for _ in range(n+1)]
        for a,b,time in times:
            adjlist[a].append((b,time))
        
        minheap = [(0,k)]
        mintimes = [float('inf')]*(n+1)

        while minheap:
            time, node = heapq.heappop(minheap)
            
            if mintimes[node]!=float('inf'):
                continue

            mintimes[node]=time
            for nei,tim in adjlist[node]:
                if mintimes[nei] == float('inf'):
                    heapq.heappush(minheap,(tim+time,nei))
        
        if float('inf') not in mintimes[1::]:
            return max(mintimes[1::])
        else:
            return -1