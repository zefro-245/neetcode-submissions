class Solution(object):
    def checkInclusion(self, s1, s2):
        k = len(s1)
        l = 0
        s1_set = Counter(s1)
        for r in range(len(s2)):
            while (r-l+1) >= k:
                s2_set = Counter(s2[l:r+1])
                if s2_set == s1_set:
                    return True
                else:
                    l+=1
        return False
        