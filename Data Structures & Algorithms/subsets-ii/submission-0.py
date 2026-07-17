class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        def backtracking(i: int, subset: List[int]):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtracking(i+1, subset)
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            subset.pop()
            backtracking(i+1, subset)
        
        backtracking(0, [])

        return result