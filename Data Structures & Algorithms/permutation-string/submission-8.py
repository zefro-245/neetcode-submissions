class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l = 0
        r = n-1
        fir = Counter(s1)
        sec = Counter(s2[:n])

        while r<len(s2):
            if fir==sec:
                return True
            else:
                sec[s2[l]]-=1
                l+=1
                r+=1
                if r==len(s2):
                    break
                elif s2[r] in sec:
                    sec[s2[r]]+=1
                else:
                    sec[s2[r]]=1
        return False