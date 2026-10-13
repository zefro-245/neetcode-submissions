class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        graph = defaultdict(list)
        for u,v,time in times:
            graph[u].append((v,time))
        
        mintimes = {}
        minheap = [(0,k)]

        while minheap:
            time_k_to_i,i = heapq.heappop(minheap)

            if i in mintimes:
                continue
            
            mintimes[i] = time_k_to_i
            for nei, nei_time in graph[i]:
                if nei not in mintimes:
                    heapq.heappush(minheap, (time_k_to_i+nei_time,nei))
        
        if len(mintimes) == n:
            return max(mintimes.values())
        else:
            return -1

