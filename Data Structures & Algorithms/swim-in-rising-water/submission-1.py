class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        min_heap = [(grid[0][0], 0, 0)]
        max_value = 0
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
        LEN = len(grid)-1

        while min_heap:
            w, row, col = heapq.heappop(min_heap)
            if grid[row][col] < 0:
                continue

            max_value = max(max_value, grid[row][col])
            grid[row][col] = -1

            if row == LEN and col == LEN:
                return max_value

            for rd, cd in directions:
                crow, ccol = row+rd, col+cd
                if min(crow, ccol) < 0 or max(crow, ccol) > LEN or grid[crow][ccol] < 0:
                    continue
                heapq.heappush(min_heap, (grid[crow][ccol], crow, ccol))

        return max_value  

