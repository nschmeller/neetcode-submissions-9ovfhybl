class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded += str(len(s))
            encoded += '#'
            encoded += s
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        cursor = 0
        length_chars = []
        while cursor < len(s):
            if s[cursor] == '#':
                cursor += 1
                length = int("".join(length_chars))
                length_chars = []
                decoded.append(s[cursor:cursor+length])
                cursor += length
            else:
                length_chars += s[cursor]
                cursor += 1

        return decoded
