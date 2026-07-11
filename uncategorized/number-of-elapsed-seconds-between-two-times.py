class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        hours = (int(endTime[:2]) - int(startTime[:2])) 
        minutes = (int(endTime[3:5]) - int(startTime[3:5]))
        seconds = (int(endTime[6:]) - int(startTime[6:]))
        return ((hours * 3600) + (minutes * 60) + seconds) % 86400