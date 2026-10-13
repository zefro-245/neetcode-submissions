class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        i = 0
        gasleft = 0
        if sum(gas)<sum(cost):
            return -1
        else:
            while i<len(gas):
                gasleft += gas[i]-cost[i]
                if gasleft<0:
                    gasleft = 0
                    res = i + 1
                i+=1
        return res
        