class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        combination = []

        def backtrack(start):
            if sum(combination) == target:
                output.append(combination.copy())
                return
            
            if sum(combination) > target:
                return
            
            for i in range(start, len(nums)):
                combination.append(nums[i])
                backtrack(i)
                combination.pop()
            
        backtrack(0)
        return output