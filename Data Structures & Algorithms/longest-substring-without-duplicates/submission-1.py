class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # My own attempt 1 day after:
        longest = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
    
            seen.add(s[right])
            longest = max(longest, len(seen))
            
        return longest
