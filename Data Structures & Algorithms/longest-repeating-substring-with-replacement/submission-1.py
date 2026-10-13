class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        maxlength = 0
        count = {}
        while r<len(s):
            if s[r] in count:
                count[s[r]]+=1
            else:
                count[s[r]]=1

            while (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
                
            maxlength = max(maxlength,r-l+1)
            r+=1
        return maxlength