class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        left = 0

        if len(s) == 1 or len(s) == 0:
            return len(s)

        for right,char in enumerate(s):
            # if it's the first case:
            if left == right:
                char_map[char] = left
                continue
            
            # if its a seen character 
            if char in char_map and char_map[char] <= right:
                left = char_map[char] + 1
            
            char_map[char] = right
            
            max_length = max(max_length, right - left + 1)
        return max_length
            
                



            
       

        # edge case:
        # if s == '':
        #     return 0
        # longest = s[0]
        # max_length = 1
        # current_length = 1
        # curr = s[0]
        # i = 1

        # while i < len(s):
        #     char = s[i]
        #     # if consecutive 
        #     if char in curr:
        #         i += 1
        #         curr = char
        #         continue
            
        #     for j in range(i, len(s)):
        #         next = s[j]
        #         if next in curr:
        #             break
        #         if next not in curr:
        #             curr += next
        #             current_length = len(curr)
            
        #     if current_length > max_length:
        #         max_length = current_length
        #         longest = curr

        #     curr = char
        # return max_length




        