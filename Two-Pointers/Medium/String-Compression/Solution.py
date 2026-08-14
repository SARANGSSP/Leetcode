class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        char1 = chars[0]
        currcount = 1
        resstr = ""
        for i in range(1, n):
            if chars[i] == char1:
                currcount += 1
            else:
                if currcount > 1:
                    resstr += char1 + str(currcount)
                else:
                    resstr += char1
                char1 = chars[i]
                currcount = 1
        if currcount > 1:
            resstr += char1 + str(currcount)
        else:
            resstr += char1

        for i in range(len(resstr)):
            chars[i] = resstr[i]
        return len(resstr)