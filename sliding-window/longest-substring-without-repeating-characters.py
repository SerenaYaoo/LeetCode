class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # 如果字符出现过，且在当前窗口 [left, right] 范围之内
            if char in char_map and char_map[char] >= left:
                left = char_map[char]+ 1
            
            char_map[char] = right # 更新当前字符的最新索引
            max_len = max(max_len, right - left + 1)
        return max_len


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




        