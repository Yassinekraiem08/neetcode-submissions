class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## My own attempt 1 day after again because the previous one was a disaster:
        longest = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            char = s[right]
            while char in seen:
                seen.remove(s[left])
                left+= 1
            
            seen.add(char)
            longest = max(longest, len(seen))
            
        return longest
            