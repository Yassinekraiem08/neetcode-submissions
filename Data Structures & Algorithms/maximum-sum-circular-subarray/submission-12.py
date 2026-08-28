class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum = nums[0]
        minsum = nums[0]
        currentmin = 0
        currentmax = 0
        totalsum = sum(nums)

        for i in range(len(nums)):
            currentmax += nums[i]
            if maxsum < currentmax:
                maxsum = currentmax
            if currentmax < 0:
                currentmax = 0
            
            currentmin += nums[i]
            if minsum > currentmin:
                minsum = currentmin
            if currentmin > 0:
                currentmin = 0
            
        if maxsum < 0:
            return maxsum
        
        return max(totalsum - minsum, maxsum)