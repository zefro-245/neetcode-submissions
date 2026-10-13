class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import Counter, deque
        taskdic = Counter(tasks)
        maxheap = [(-x[1],x[0]) for x in taskdic.items()]
        heapq.heapify(maxheap)
        count = 0
        deque = deque()

        while maxheap or deque:
            if deque and deque[0][2]<=count:
                freq,task,av_time = deque.popleft()
                heapq.heappush(maxheap, (-freq, task))
            if maxheap:
                freq, task = heapq.heappop(maxheap)
                freq = -freq
                freq = freq-1         
                if freq:
                    deque.append((freq,task,count+n+1))
                count+=1
            else:
                count+=1
        return count