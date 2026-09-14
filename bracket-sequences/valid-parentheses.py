class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}': '{'}
        stack = []

        for char in s:
            if char in mapping: # if its a right parenthesis
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
                
            else:
                # if it's a left parenthesis, add it to the stack
                stack.append(char)
        # only valid if the stack is empty
        return not stack

