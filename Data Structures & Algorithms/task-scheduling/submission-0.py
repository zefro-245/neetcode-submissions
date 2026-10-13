class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskdic = Counter(tasks)
        self.maxHeap = [-x for x in taskdic.values()]
        heapq.heapify(self.maxHeap)
        count = 0

        while len(self.maxHeap):
            temp = []
            executed = 0
            for i in range(n+1):
                if self.maxHeap:
                    freq = heapq.heappop(self.maxHeap)
                    freq += 1
                    executed += 1

                    if freq != 0:
                        temp.append(freq)
            if temp:
                count += n + 1
            else:
                count += executed
            for i in temp:
                heapq.heappush(self.maxHeap, i)
        return count

