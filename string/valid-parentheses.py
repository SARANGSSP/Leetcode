class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_brackets = ['(', '[', '{']
        close_brackets = [')', ']', '}']
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif char in close_brackets:
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
        
        return not stack