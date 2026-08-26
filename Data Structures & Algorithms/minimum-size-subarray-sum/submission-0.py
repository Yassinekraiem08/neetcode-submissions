class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        subarray_count = float('inf')
        left = 0
        right = 0
        current_sum = 0

        while right < len(nums):
            current_sum += nums[right]
            
            while current_sum >= target:
                subarray_count = min(subarray_count, right - left + 1)
                current_sum -= nums[left]
                left += 1
            right += 1
        

        return subarray_count if subarray_count != float('inf') else 0