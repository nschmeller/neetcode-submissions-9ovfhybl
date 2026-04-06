class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = carry = 0

        for i in range(32):
            a_bit, b_bit = a >> i & 1, b >> i & 1
            curr_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            res |= curr_bit << i
        
        if res > 2 ** 31 - 1:
            res = ~(res ^ 2 ** 32 - 1)

        return res
