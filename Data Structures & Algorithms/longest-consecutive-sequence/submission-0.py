class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        numset = set(nums)


        for number in numset:
            if number - 1 in numset:
                continue
            else:
                current_length = 1
                while number + 1 in numset:
                    current_length += 1
                    number += 1
            
            longest = max(longest, current_length)
        
        return longest