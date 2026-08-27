class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currentmax = 0
        currentmin = 0
        minsum = nums[0]
        totalsum = sum(nums)

        for i in range (len(nums)):
    
            if currentmax < 0:
                currentmax = 0
            currentmax += nums[i]
            if currentmax > maxsum:
                maxsum = currentmax

            
            if currentmin > 0:  
                currentmin = 0
            currentmin += nums[i]
            if currentmin < minsum:
                minsum = currentmin

        if maxsum < 0:
            return maxsum

        return max(totalsum - minsum, maxsum)   
            
            