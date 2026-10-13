class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        store = {}
        maxfreq = 0
        ans = 0

        for r in range(len(s)):
            store[s[r]] = store.get(s[r],0) + 1
            maxfreq = max(store[s[r]],maxfreq)

            while (r-l+1) - maxfreq > k:
                store[s[l]] -= 1
                l+=1
            ans = max(r-l+1, maxfreq)
        return ans