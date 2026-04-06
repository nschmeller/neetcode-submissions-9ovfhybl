class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        length_chars = []
        while curr < len(s):
            if s[curr] == '#':
                curr += 1
                length = int("".join(length_chars))
                res.append(s[curr:curr+length])
                curr += length
                length_chars = []
            else:
                length_chars += s[curr]
                curr += 1
        return res
