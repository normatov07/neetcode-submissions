class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 

        def backtracking(i: int):
            if len(nums) == i:
                res.append(nums.copy())
                return
            
            seen = set()
            for j in range(i, len(nums)):
                if nums[j] in seen:
                    continue

                seen.add(nums[j])
                
                nums[i], nums[j] = nums[j], nums[i]
                backtracking(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtracking(0)

        return res
    

# 0  1,1,2 ; 1,2,1;  
#     1  1,1,2 ; 1,2,1
#         2 -> 1,1,2
