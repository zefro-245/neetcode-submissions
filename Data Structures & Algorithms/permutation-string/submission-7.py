class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l = 0
        r = n-1
        while r<len(s2):
            if Counter(s1)==Counter(s2[l:r+1]):
                return True
            else:
                l+=1
                r+=1
        return False