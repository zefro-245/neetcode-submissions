class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        conv = ""
        for i in digits:
            conv+=str(i)
        convplus = int(conv)+1
        convconv = str(convplus)
        for j in convconv:
            res.append(int(j))
        return res
        