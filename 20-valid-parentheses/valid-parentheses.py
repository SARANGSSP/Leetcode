class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        top = -1
        pair = {")":"(","]":"[","}":"{"}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
                top += 1
            else:
                a = pair.get(ch)
                if top > -1 and stack[top] == a:
                    stack.pop()
                    top -= 1
                else:
                    return False
        if top == -1:
            return True
        else:
            return False

