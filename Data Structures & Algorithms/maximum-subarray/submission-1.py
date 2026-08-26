class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #optimal solution(without tracking the subarray indices):
        maxsum = nums[0]
        currentsum = 0
        for right in range(len(nums)):
            if currentsum < 0:
                currentsum = 0

            currentsum += nums[right]
            maxsum = max(maxsum, currentsum)
        
        return maxsum