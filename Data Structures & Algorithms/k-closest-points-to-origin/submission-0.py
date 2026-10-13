class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in points:
            dist.append([math.sqrt(i[0]**2+i[1]**2),i])
        self.maxHeap = [[-x[0],x[1]] for x in dist]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) > k:
            heapq.heappop(self.maxHeap)
        
        ans = []
        for j in self.maxHeap:
            ans.append(j[1])
        return ans


