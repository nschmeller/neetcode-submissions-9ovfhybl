class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i, bit in enumerate(
            reversed(
                [1 if n & (1 << i) else 0 for i in range(32)]
            )
        ):
            if bit:
                res |= 1 << i
        
        return res
