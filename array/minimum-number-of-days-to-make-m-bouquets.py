class Solution:
    # if k * m > len of the arr we have to return -1 since one flower can only be used in one bouqet
    # what is my l and r ? I think my l is the min no of day in the arr and my r is the max no of days
    #next step is to check if the flower blooms on a given day( to check my idea is to subtratct the current day from the day in the array and if its 0 or less than that make it zero in a temp arr)
    #then for every day we check if we are able to make the number of subarrays of contiguous elements on any given day, if we are we remove the right of mid to find the exact no of days
    #how to find the correct contiguous array ? we make a counter and count consecutive as soon as it hits the given req we set it to zero again or if its not 0, we set it to zero and return the no of days as soon as we get m no of bouqets
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k > n:
            return -1
        l=min(bloomDay)
        r=max(bloomDay)
        ans=-1
        while(l<=r):
            mid=l+(r-l)//2
            count=0
            op=0
            for day in bloomDay:
                if day<=mid:
                    count+=1
                else:
                    op=op+(count//k)
                    count=0 
            op=op+(count//k) 
            if op>=m:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans