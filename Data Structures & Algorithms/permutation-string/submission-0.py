from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        k = len(s1)
        
        if k > len(s2):
            return False

        need = Counter(s1)
        window = Counter()

        l = 0

        for r in range(len(s2)):
            window[s2[r]] += 1

            # Keep window size at k
            if r - l + 1 > k:
                window[s2[l]] -= 1
                l += 1

            # Compare frequencies
            if window == need:
                return True

        return False