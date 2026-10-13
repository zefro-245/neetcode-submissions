class Solution:
    def isValid(self, s: str) -> bool:
        val = {')':'(','}':'{',']':'['}
        if s=="":
            return True
        stack = []
        i=0
        for i in range(len(s)):
            if s[i] in ')}]':
                if not(stack):
                    return False
                lastele = stack.pop()
                if not(val[s[i]]==lastele):
                    return False
            elif s[i] in '({[':
                stack.append(s[i])
            i+=1
        if not(stack):
            return True
        else:
            return False