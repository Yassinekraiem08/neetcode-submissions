class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        subsets = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                output.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            backtrack(i+1)
            subsets.pop()
            

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i +=1 

            backtrack(i+1)
            
        backtrack(0)
        return output