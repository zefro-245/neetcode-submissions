class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramlist = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagramlist[sorted_s].append(s)
        return list((anagramlist.values()))



        
        