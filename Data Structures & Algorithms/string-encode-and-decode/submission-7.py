class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        res = []
        prev = curr = 0

        while curr < len(s):
            if s[curr] == "#":
                res.append(s[curr+1:curr+1+int(s[prev:curr])])
                prev = curr = curr + int(s[prev:curr]) + 1
            else:
                curr += 1
        
        return res
