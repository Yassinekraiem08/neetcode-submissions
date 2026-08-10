class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Optimized Solution:
        container = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            width = j - i
            water_height = min(heights[i], heights[j])
            current_area = water_height * width
            container = max(container, current_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return container