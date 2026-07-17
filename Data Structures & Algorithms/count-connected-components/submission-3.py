class UnionFind:

    def __init__(self, length):
        self.parent = [i for i in range(length)]
        self.size = [1] * length


    def find(self, num: int) -> int:
        while num != self.parent[num]:
            self.parent[num] = self.find(self.parent[num])
            num = self.parent[num]

        return num

    def union(self, num1: int, num2: int) -> int:
        pr1 = self.find(num1)
        pr2 = self.find(num2)

        if pr1 == pr2: return

        if self.size[pr1] > self.size[pr2]:
            pr2, pr1 = pr1, pr2
        
        self.parent[pr1] = pr2
        self.size[pr2] += self.size[pr1]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uni_find = UnionFind(n)

        for edg1, edg2 in edges:
            uni_find.union(edg1, edg2)
        
        visited = set()
        count = 0
        for edg1 in range(n):
            parent = uni_find.find(edg1)
            count += (parent not in visited)
            visited.add(parent)

        
        return count