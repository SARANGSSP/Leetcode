class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x, n):
            if n == 0:
                return 1.0
            if n == 1:
                return x
            if n % 2 == 0:
                return power(x * x, n // 2)
            return x * power(x, n - 1)

        if n < 0:
            return 1.0 / power(x, -n)
        return power(x, n)