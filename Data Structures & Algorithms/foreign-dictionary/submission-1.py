class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        order = ""
        g = defaultdict(list)
        for word in words:
            for c in word:
                g[c] = []
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2):
                if w1[:len(w2)] == w2:
                    return ""

            for j in range(len(w1)):
                if w1[j] != w2[j]:
                    g[w1[j]].append(w2[j])
                    break
        
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = {}
        for c in g:
            states[c] = UNVISITED

        def dfs(i):
            nonlocal order
            if states[i] == VISITING:
                return False
            elif states[i] == VISITED:
                return True
            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei):
                    return False
            states[i] = VISITED
            order+=i
            return True
        
        for c in g:
            if not dfs(c):
                return ""

        return order[::-1]