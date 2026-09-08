class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        

        output = []

        current = []

        def backtrack(i):
            if not digits:
                return []
            if i == len(digits):
                output.append("".join(current))
                return
            
            letters = phone[digits[i]]

            for char in letters:
                current.append(char)
                backtrack(i + 1)
                current.pop()
        
        backtrack(0)

        return output

            
