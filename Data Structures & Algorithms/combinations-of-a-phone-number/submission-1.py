class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        num_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def backtracking(i: int, c: List[str]):
            if len(digits) == len(c):
                res.append("".join(c.copy()))
                return

            if i >= len(digits):
                return
            
            for ch in num_to_char[digits[i]]:
                c.append(ch)
                backtracking(i+1, c)
                c.pop()
        
        backtracking(0, [])

        return res