class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = strs[0]

        for word in strs:
            while not word.startswith(longest) and longest != '':
                longest = longest[:-1]
        return longest

        
