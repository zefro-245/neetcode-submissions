class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-x for x in stones]
        if len(self.maxHeap) == 0:
            return 0
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap) > 1:
            x = heapq.heappop(self.maxHeap)
            y = heapq.heappop(self.maxHeap)

            if x != y:
                heapq.heappush(self.maxHeap, (x-y))
        
        if len(self.maxHeap) == 1:
            return self.maxHeap[0]*(-1)
        else:
            return 0
