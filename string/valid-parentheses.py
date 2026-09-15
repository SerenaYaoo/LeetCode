class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}': '{'}
        stack = []

        for char in s:
            # this char is a right parenthesis
            if char in mapping:
                if stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack

            

        

