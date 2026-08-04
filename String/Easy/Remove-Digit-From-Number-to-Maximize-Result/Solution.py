class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        last_idx = -1
        for i in range(n):
            if number[i] == digit:
                last_idx = i
                if i + 1 < n and number[i] < number[i+1]:
                    return number[:i] + number[i+1:]
        return number[:last_idx] + number[last_idx+1:]