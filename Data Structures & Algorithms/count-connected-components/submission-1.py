class DSU:
    def __init__(self,n):
        self.comps = n
        self.Parent = list(range(n+1))
        self.Size = [1]*(n+1)
    def find(self,node):
        if self.Parent[node]!=node:
            self.Parent[node]=self.find(self.Parent[node])
        return self.Parent[node]
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)

        if pu==pv:
            return False

        self.comps-=1
        if self.Size[pu]<self.Size[pv]:
            pu,pv=pv,pu
        self.Parent[pv]=pu
        self.Size[pu]+=self.Size[pv]
        return True
    def components(self):
        return self.comps

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u,v in edges:
            dsu.union(u,v)
        return dsu.components()
        