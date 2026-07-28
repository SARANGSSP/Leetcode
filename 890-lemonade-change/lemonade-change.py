class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        count5,count10,count20,totalcount = 0,0,0,0
        for i in range(n):
            if bills[i] == 5:
                count5 += 1
                totalcount += 1
                print(f"add5")
            elif bills[i] == 10:
                count10 += 1
                print(f"add10")
                if count5 > 0:
                    totalcount += 1
                    count5 -= 1
            else:
                count20 += 1
                print(f"add20")
                if count5 > 0 and count10 > 0:
                    count10 -= 1
                    count5 -= 1
                    totalcount += 1
                elif count5 >= 3:
                    count5 -= 3
                    totalcount += 1
        if totalcount == n:
            return True
        else:
            print(totalcount)
            return False