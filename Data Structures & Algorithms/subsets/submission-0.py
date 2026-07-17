class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtracking(i:int, subset: List[int]):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtracking(i+1, subset)
            subset.pop()
            backtracking(i+1, subset)
        
        backtracking(0, [])

        return result