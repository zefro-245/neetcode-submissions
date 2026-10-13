from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        need = Counter(t)
        window = Counter()

        have = 0
        required = len(need)

        l = 0
        best = ""

        for r in range(len(s)):

            # Add character to window
            window[s[r]] += 1

            # This character's requirement is now satisfied
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1

            # Window is valid
            while have == required:

                # Update answer
                if not best or (r - l + 1) < len(best):
                    best = s[l:r+1]

                # Remove left character
                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1

        return best