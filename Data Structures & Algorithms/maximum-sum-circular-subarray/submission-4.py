class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum = nums[0]
        minsum = nums[0]
        total = sum(nums)
        maxcurrent = 0
        mincurrent = 0
        

        for i in range(len(nums)):
            maxcurrent += nums[i]
            if maxcurrent > maxsum:
                maxsum = maxcurrent
            if maxcurrent < 0:
                maxcurrent = 0

            mincurrent += nums[i]
            if mincurrent < minsum:
                minsum = mincurrent
            if mincurrent > 0:
                mincurrent = 0
            
        if maxsum < 0:
            return maxsum

        return max(total - minsum, maxsum)