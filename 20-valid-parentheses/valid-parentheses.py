class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        validmapping = { "]":"[",")": "(","}":"{"}
        stack = []
        for char in s:
            if char in validmapping.values():
                stack.append(char)
            else:
                if len(stack) != 0:
                    opening = stack.pop()
                    if opening != validmapping[char]:
                        return False
                else:
                    return False
                    
        if len(stack) == 0:
            return True
        else:
            return False