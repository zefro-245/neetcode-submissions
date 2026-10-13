class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}

        res, sol = [], []

        def dfs(i):
            if i == len(digits):
                res.append("".join(sol))
                return

            for letter in phone[digits[i]]:
                sol.append(letter)
                dfs(i+1)
                sol.pop()
        dfs(0)
        return res