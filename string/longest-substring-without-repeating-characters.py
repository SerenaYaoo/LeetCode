class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = s[0]
        max_length = 1
        current_length = 1
        curr = s[0]
        i = 1

        while i < len(s):
            char = s[i]
            # if consecutive 
            if char in curr:
                i += 1
                curr = char
                continue
            
            for j in range(i, len(s)):
                next = s[j]
                if next in curr:
                    break
                if next not in curr:
                    curr += next
                    current_length = len(curr)
            
            if current_length > max_length:
                max_length = current_length
                longest = curr
                
            curr = char
        return max_length




        