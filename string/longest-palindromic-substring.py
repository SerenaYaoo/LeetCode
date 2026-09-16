class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        res = ""

        def expand(left: int, right:int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        for i in range(len(s)):
            sub1 = expand(i, i)
            sub2 = expand(i, i+1)

            if len(sub1) > len(res):
                res = sub1
            if len(sub2) > len(res):
                res = sub2
        return res


        