class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        combination = []

        def backtrack(start):
            if sum(combination) == target:
                output.append(combination.copy())
                return
            
            if sum(combination) > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtrack(i + 1)
                combination.pop()

            
        backtrack(0)
        return output
