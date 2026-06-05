class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if not s:
            return 0
        sig = 1
        i=0
        if s[0]=='+':
            i+=1
        elif s[0]=='-':
            i+=1
            sig=-1
        n = len(s)
        st = i
        while i<n and s[i].isdigit():
            i+=1
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if i>st:
            if sig==1 and int(s[st:i])<INT_MAX:
                return int(s[st:i])
            elif sig==-1 and -int(s[st:i])>INT_MIN:
                return -int(s[st:i])
            elif sig==-1:
                return INT_MIN
            else:
                return INT_MAX
        else:
            return 0


        