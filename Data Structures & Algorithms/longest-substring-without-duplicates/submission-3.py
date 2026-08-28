class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = set()
        left = 0
        right = 0

        while right < len(s):
            
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            right += 1

            longest = max(longest, len(window))
        
        return longest