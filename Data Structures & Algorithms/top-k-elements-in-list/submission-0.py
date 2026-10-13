class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        done = {}
        for i in nums:
            done[i] = 1 + done.get(i,0)
        
        arr = []
        for key,val in done.items():
            arr.append([val,key])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
