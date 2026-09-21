class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute force solution O(n^2)
        """
       for i in range (len(nums)):
           for j in range(i+1, len(nums)):
               if nums[i] + nums[j] == target:
                   return [i,j]
        """
        # Optimized solution O(n)
        # Create an empty dictionary where we will store each number we have already seen and its index.
        hashmap = {}

        for index, number in enumerate(nums):

            complement = target - number

            if complement in hashmap:
                
                return [hashmap[complement], index]
                
            hashmap[number] = index