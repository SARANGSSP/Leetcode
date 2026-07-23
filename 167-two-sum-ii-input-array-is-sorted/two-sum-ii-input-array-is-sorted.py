class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 2:
            return [1,2]
        i = 0
        j = n-1
        while i < j:
            if numbers[j] + numbers[i] == target:
                return [i+1,j+1]
            elif numbers[j] + numbers[i] > target:
                j -= 1
            else:
                i += 1
