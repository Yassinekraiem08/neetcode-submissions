class Solution:
    def trap(self, height: List[int]) -> int:
        # Optimized Solution:
        trapped_water = 0
        left = 0
        right = len(height) - 1
        leftmax = height[left]
        rightmax = height[right]

        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax, height[left])
                trapped_water += leftmax - height[left]

            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                trapped_water += rightmax - height[right]

        return trapped_water