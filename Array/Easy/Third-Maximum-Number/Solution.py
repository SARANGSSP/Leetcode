class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = list(set(nums))
        fmax = float(-inf)
        smax = float(-inf)
        tmax = float(-inf)
        if len(a) < 3:
            return max(a)
        else:
            for i in range(len(a)):
                if a[i] > fmax:
                    tmax,smax,fmax = smax,fmax,a[i]
                elif a[i] > smax :
                    smax,tmax = a[i],smax
                elif a[i] > tmax:
                    tmax = a[i]
            return tmax