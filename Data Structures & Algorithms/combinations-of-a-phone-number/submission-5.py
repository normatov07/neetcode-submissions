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

        res = deque()
        for v in num_to_char[digits[0]]:
            res.append(v)

        for i in range(1, len(digits)):
            for _ in range(len(res)):
                curr = res.popleft()
                for ch in num_to_char[digits[i]]:
                    res.append(curr+ch)
        
        return list(res)