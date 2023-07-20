class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * len(par)

        def find(n1):
            node = n1
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += p1
            return True

        for a , b in edges:
            if not union(a,b):
                return[a,b]



