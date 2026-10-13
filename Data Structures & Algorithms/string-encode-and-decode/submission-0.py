class Solution:

    def encode(self, strs: List[str]) -> str:
        stringy = ""
        for i in strs:
            stringy = stringy + str(len(i)) + "#" + i
        return stringy

    def decode(self, s: str) -> List[str]:
        out = []
        j = 0
        while j < len(s):
            k = j
            while s[k] != "#":
                k+=1
            length = int(s[j:k])
            word = s[k+1:k+1+length]
            out.append(word)
            j = k+length+1
        return out



