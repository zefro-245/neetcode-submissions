class Solution:
    def isPalindrome(self, s: str) -> bool:
        straight = ""
        for i in s:
            if i.isalnum():
                straight += i.lower()
        if straight == straight[::-1]:
            return True
        else:
            return False



        