class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Optimized solution:
        
        longest = 0
        left = 0 
        count = {}
        for right in range(len(s)):
            char = s[right]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

            current_length = right - left + 1
            max_frequency = max(count.values())
            replacements_needed = current_length - max_frequency
            
            while replacements_needed > k:
                count[s[left]] -= 1
                left += 1
                current_length = right - left + 1
                max_frequency = max(count.values())
                replacements_needed = current_length - max_frequency

            longest = max(longest, current_length)
        
        return longest