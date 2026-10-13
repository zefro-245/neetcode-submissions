from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Use a set to prevent duplicate edges
        adjlist = defaultdict(set)
        
        # Correctly initialize indegree for all unique characters
        indegree = {c: 0 for word in words for c in word}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            # Invalid case: w1 is longer and w2 is a prefix of w1
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
                
            # Find the first non-matching character
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    # Only update indegree if it's a new edge
                    if w2[j] not in adjlist[w1[j]]:
                        adjlist[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque() 
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)    

        res = []
        while q:
            char = q.popleft()
            res.append(char)
            for nei in adjlist[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    
        if len(res) != len(indegree):
            return ""
            
        return "".join(res)