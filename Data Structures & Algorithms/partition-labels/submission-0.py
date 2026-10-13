class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last = 0
        start = 0
        store = {}
        j = 0
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] not in store:
                store[s[i]] = i
        while j<len(s):
            last = max(last,store[s[j]])
            if j==last:
                res.append(last-start+1)
                last = 0
                start = j+1
            j+=1
        return res