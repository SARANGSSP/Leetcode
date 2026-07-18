class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        string = ""
        i = 0
        counter = 0
        for char in s:
            if char == y:
                counter += 1
            else:
                string += char
        return (counter*y) + string