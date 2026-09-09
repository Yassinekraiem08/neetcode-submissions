class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        permutation = []
        count = Counter(nums)

        def backtrack(i):
            if len(permutation) == len(nums):
                output.append(permutation.copy())
                return
        
            for num in count:
                if count[num] == 0:
                    continue

                permutation.append(num)
                count[num] -= 1
                backtrack(i+1)
                count[num] += 1
                permutation.pop()
        
        backtrack(0)
        return output