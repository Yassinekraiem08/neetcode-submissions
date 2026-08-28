class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        longest = 1
        left = 0

        for right in range(1, len(arr)):

            if arr[right] - arr[right - 1] == 0:
                left = right

            elif right > 1:
                previous = arr[right - 1] - arr[right - 2]

                # Same direction twice -> turbulence breaks
                if (arr[right] - arr[right - 1] > 0 and previous > 0) or (arr[right] - arr[right - 1] < 0 and previous < 0):
                    left = right - 1

            longest = max(longest, right - left + 1)

        return longest