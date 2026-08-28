class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        count = Counter()
        for right in range(len(s)):
            count[s[right]] += 1
            
            current_length = right - left + 1 
            replacements_needed = current_length - max(count.values())

            if replacements_needed > k:
                count[s[left]] -= 1
                left += 1
                current_length = right - left + 1 
                
                replacements_needed = current_length - max(count.values())

            longest = max(longest, current_length)

        return longest