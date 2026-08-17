class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def double(arr):
            arr.append(arr[-1]*2)
        def invalidate(arr):
            a = arr.pop()
        def add(num,arr):
            arr.append(arr[-1] + arr[-2])
        def arrsum(arr):
            if len(arr) >= 2:
                arr.append(arr[-1] + arr[-2])
            else:
                arr.append(arr[-1])
        res = []
        for ele in operations:
            if ele == "D":
                double(res)
            elif ele == "C":
                invalidate(res)
            elif ele == "+":
                arrsum(res)
            else:
                res.append(int(ele))
        return sum(res)
        


