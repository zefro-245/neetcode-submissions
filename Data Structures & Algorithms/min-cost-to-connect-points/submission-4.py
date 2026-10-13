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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
            
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
        edges.sort()
        
        uf = DSU(n)
        min_cost = 0
        edges_used = 0

        for cost,i,j in edges:
            if uf.union(i,j):
                min_cost+=cost
                edges_used+=1

                if edges_used == n-1:
                    return min_cost
        