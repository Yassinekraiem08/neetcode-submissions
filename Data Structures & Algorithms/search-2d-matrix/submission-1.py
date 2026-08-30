class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for tables in matrix:
            left = 0
            right = len(tables) - 1

            while left <= right:
                middle  = (left + right) // 2

                if tables[middle] == target:
                    return True

                elif tables[middle] < target:
                    left = middle + 1
                elif tables[middle] > target:
                    right = middle - 1

        return False