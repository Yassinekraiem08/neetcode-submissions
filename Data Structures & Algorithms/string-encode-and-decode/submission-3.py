class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            word_length = int(s[i:j])

            word_start = j + 1

            word_end = word_start + word_length
            
            word = s[word_start:word_end]
            decoded_strs.append(word)

            i = word_end
        
        return decoded_strs