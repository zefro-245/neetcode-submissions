class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        res, sol = [], ""
        n = len(digits)
        phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}

        def dfs(i,sol):
            if i==n:
                res.append(sol)
                return
            for j in range(len(phone[digits[i]])):
                dfs(i+1,sol+phone[digits[i]][j])
        dfs(0,sol)
        return res
