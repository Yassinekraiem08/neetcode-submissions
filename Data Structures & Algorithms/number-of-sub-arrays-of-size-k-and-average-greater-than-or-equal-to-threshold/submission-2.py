class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarray = 0
        left = 0
        right = k - left - 1
        currentsum = sum(arr[left:right+1])

        while right < len(arr):

            if currentsum / k >= threshold:
                subarray += 1

            
            if right + 1 < len(arr):
                currentsum = currentsum - arr[left] + arr[right+1]
            
            left += 1
            right += 1
                    

        return subarray