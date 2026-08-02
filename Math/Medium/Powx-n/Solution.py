class Solution:
    def power(self, x, n):
        # Base case: anything raised to 0 is 1
        if n == 0:
            return 1.0
        
        # Base case: anything raised to 1 is itself
        if n == 1:
            return x
        
        # If 'n' is even
        if n % 2 == 0:
            # Recursive call: x * x, n // 2
            return self.power(x * x, n // 2)
        
        # If 'n' is odd
        # Recursive call: x * power(x, n - 1)
        return x * self.power(x, n - 1)

    def myPow(self, x, n):
        # If 'n' is negative
        if n < 0:
            # Calculate the power of -n and take reciprocal
            return 1.0 / self.power(x, -n)
        
        # If 'n' is non-negative
        return self.power(x, n)