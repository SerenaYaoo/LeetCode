class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = s[0]
        max_length = 1
        current_length = 1
        curr = s[0]

        for char in s[1:]:
            # print(char)
            if char not in curr:
                curr += char
                current_length = len(curr)
                # print(curr)

            else:
                curr = char
            
            if current_length > max_length:
                
                max_length = current_length
                longest = curr
        return max_length




        