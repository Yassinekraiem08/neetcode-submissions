class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxcontainer = 0
        left = 0
        right = len(heights) - 1

        while left != right:
            water_height = min(heights[left], heights[right])
            width = right - left
            current_container = water_height * width

            maxcontainer = max(maxcontainer ,current_container)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1 

        return maxcontainer