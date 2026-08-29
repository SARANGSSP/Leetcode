class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        num = int((5/100)*n)
        res_arr = sorted(arr)[num:n-num]
        return float(f"{sum(res_arr)/len(res_arr):.5f}")
        