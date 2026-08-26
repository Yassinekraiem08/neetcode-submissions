class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        output = 0
        left = 0
        right = left + k - 1
        current_sum = sum(arr[left:right+1])
        while right < len(arr):

            if  current_sum / k >= threshold:
                output += 1

            if right + 1 < len(arr):
                current_sum = current_sum - arr[left] + arr[right + 1]
        
            left += 1
            right += 1
            
        return output