from dataclasses import dataclass

@dataclass
class Combination:
    cb: list
    sm: int



class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.nums = nums
        self.target = target
        self.backtracking(0, Combination(cb=[], sm=0))

        return self.result

    
    def backtracking(self, i: int, c: Combination):
        if c.sm == self.target:
            self.result.append(list(c.cb))
            return

        if i >= len(self.nums) or c.sm > self.target:
            return

       
        c.cb.append(self.nums[i])
        c.sm += self.nums[i]
        self.backtracking(i, c)
        
        
        c.cb.pop()
        c.sm -= self.nums[i]
        self.backtracking(i + 1, c)