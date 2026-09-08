class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        current = []

        def backtrack(start):
            if sum(current) == target:
                output.append(current.copy())
                return

            if sum(current) > target:
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i)
                current.pop()

        backtrack(0)

        return output