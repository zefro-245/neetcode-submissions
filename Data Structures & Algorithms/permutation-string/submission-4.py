class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        k = len(s1)
        r = 0
        while r<len(s2):
            if Counter(s2[r:r+k]) == c1:
                return True
            elif not s2[r:r+k]:
                return False
            else:
                r += 1
        return False