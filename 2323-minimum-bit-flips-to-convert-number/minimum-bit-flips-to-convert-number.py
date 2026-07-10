class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startbin = str(bin(start))[2::]
        goalbin = str(bin(goal))[2::]
        n = len(startbin)
        m = len(goalbin)
        if n >= m:
            goalbin = "0"*(n-m) + goalbin
        else:
            startbin = "0"*(m-n) + startbin
        steps = 0
        for i in range(len(startbin)):
            if startbin[i] != goalbin[i]:
                steps += 1
        return steps
