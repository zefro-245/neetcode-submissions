class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.maxHeap = [-x for x in nums]
        heapq.heapify(self.maxHeap)

        for i in range(k-1):
            heapq.heappop(self.maxHeap)
        return self.maxHeap[0]*(-1)