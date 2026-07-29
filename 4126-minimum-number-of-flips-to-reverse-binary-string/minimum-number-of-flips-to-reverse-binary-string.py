class Solution:
    def minimumFlips(self, n: int) -> int:

        return (n ^ int(bin(n)[~0:1:-1], 2)).bit_count()
        