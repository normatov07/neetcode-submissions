class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(float('inf'), i) for i in range(len(points))]
        res = 0

        while heap:
            w, index = heapq.heappop(heap)

            if w != float('inf'):
                res+=w
            
            for heap_index, (old_w, i) in enumerate(heap):
                new_w = abs(points[index][0]-points[i][0]) + abs(points[index][1]-points[i][1])

                if old_w > new_w:
                    heap[heap_index] = (new_w, i)
            
            heapq.heapify(heap)
        
        return res


