class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for number, frequency in count.items():
            if frequency > 1:
                return number