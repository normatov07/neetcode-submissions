class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        min_heap = [(0, 0)]
        visited = set()
        res = 0
        
        while min_heap and len(visited) != len(points):
            w, index = heapq.heappop(min_heap)
            
            if index in visited:
                continue
            
            res += w
            visited.add(index)
            
            x, y = points[index]
            for i, (x1, y1) in enumerate(points):
                if i not in visited:
                    heapq.heappush(min_heap, (abs(x-x1)+abs(y-y1), i))
        
        return res


