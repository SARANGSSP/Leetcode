#we need to set low = min(arr)
#we need to set the high to sum(arr)
#then for mid we check 
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        n = len(weights)
        while low <= high:
            mid = (low+high)//2
            day = 1
            sumi = 0 
            for i in range(n):
                if sumi < mid and (sumi + weights[i]) <= mid:
                    sumi += weights[i]
                else:
                    day += 1
                    sumi = weights[i]

            if day <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low 
            
                
                
