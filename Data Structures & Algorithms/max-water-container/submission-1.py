class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_container = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left 
            water_height = min(heights[left], heights[right])
            current_container = width * water_height
            max_container = max(max_container, current_container)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_container