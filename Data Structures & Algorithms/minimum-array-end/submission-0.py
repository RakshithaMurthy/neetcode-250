class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1  # we fill using n-1
        result = x

        bit = 0  # position in result

        while n > 0:
            # if this bit in x is 0 → we can use it
            if (x & (1 << bit)) == 0:
                # take lowest bit from n
                if (n & 1):
                    result |= (1 << bit)
                n >>= 1
            bit += 1

        return result