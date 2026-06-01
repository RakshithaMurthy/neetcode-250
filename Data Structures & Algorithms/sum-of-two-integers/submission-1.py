class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        while b != 0:
            sum_ = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            
            a = sum_
            b = carry
        
        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)
