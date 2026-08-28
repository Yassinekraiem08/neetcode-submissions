class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimal_length = float ("inf")
        current_length = 0
        left = 0
        right = 0
        for right in range(len(nums)):

            while sum(nums[left:right+1]) >= target:
                current_length = right - left + 1
                minimal_length = min(minimal_length, current_length)
                left += 1


        return 0 if minimal_length == float ("inf") else minimal_length