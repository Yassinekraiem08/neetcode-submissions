class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Optimized Solution:
        nums = sorted(nums)
        output = []
        for i in range (len(nums)):
            left = i + 1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    if [nums[i], nums[left], nums[right]] not in output:
                        output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
        return output


        