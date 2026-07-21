class UnionFind:

    def __init__(self, length: int):
        self.parent = [i for i in range(length)]
        self.size = [1] * length
        self.maxSize = 1
    
    def find(self, child: int) -> int:
        
        while self.parent[child] != child:
            self.parent[child] = self.find(self.parent[child])
            child = self.parent[child]
        
        return child

    def union(self, child1: int, child2: int):
        p1, p2 = self.find(child1), self.find(child2)

        if p1 == p2:
            return False
        
        if p1 > p2:
            p1, p2 = p2, p1
        
        self.parent[p1] = p2
        self.size[p2] += self.size[p1]
        self.maxSize = max(self.size[p2], self.maxSize)

        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for index, (a,b,w) in enumerate(edges):
            edges[index] = (w,a,b,index)
        
        edges.sort()

        def calculateMstSum(index: int, include: bool):
            minSum = 0
            uf = UnionFind(n)
            if include:
                uf.union(edges[index][1], edges[index][2])
                minSum += edges[index][0]


            for idx, (w,a,b,i) in enumerate(edges):
                if index == idx:
                    continue
                if uf.union(a,b):
                    minSum+=w

            return minSum if uf.maxSize == n else float('inf')
        
        critical = []
        pseudoCritical = []
        mst = calculateMstSum(-1, False)
        
        for index in range(len(edges)):
            if mst < calculateMstSum(index, False):
                critical.append(edges[index][3])
            elif calculateMstSum(index, True) == mst:
                pseudoCritical.append(edges[index][3])

        return [critical, pseudoCritical]