class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hasht = Counter(t)
        l=0
        r=0
        cnt = 0
        minlen = float('inf')
        sind = -1
        while r<len(s):
            if hasht[s[r]]>0:
                cnt+=1
            hasht[s[r]]-=1
            while cnt==len(t):
                if (r-l+1)<minlen:
                    minlen = r-l+1
                    sind = l
                hasht[s[l]]+=1
                if hasht[s[l]]>0:
                    cnt-=1
                l+=1
            r+=1
        if sind == -1:
            return ""
        else:
            return s[sind:sind+minlen]
