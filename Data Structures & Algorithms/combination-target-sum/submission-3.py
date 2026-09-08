class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # one day after
        output = []
        
        comb = []

        def backtrack(start):
            if sum(comb) == target:
                output.append(comb.copy())
                return

            if sum(comb) > target:
                return
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i)
                comb.pop()

        backtrack(0)
        return output