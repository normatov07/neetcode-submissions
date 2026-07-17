class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        min_heap = [(1, start_node)]
        adj_list = [[] for _ in range(n)]

        for i, (s, e) in enumerate(edges):
            adj_list[s].append((e, succProb[i]))
            adj_list[e].append((s, succProb[i]))
        
        visited = set()
        while min_heap:
            prob, index = heapq.heappop_max(min_heap)
            if index in visited:
                continue
            
            if index == end_node:
                return prob

            visited.add(index)

            for adj_index, adj_prob in adj_list[index]:
                if adj_index in visited:
                    continue
                heapq.heappush_max(min_heap, (prob*adj_prob, adj_index))
            
        
        return 0
