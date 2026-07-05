import random
class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        i = 0
        while i < n-1 :
            a = random.randint(-1*n,n)
            if a not in arr:
                arr.append(a)
                i = i+1
        arr.append(-1*sum(arr))
        return arr
