class Solution:
    def numDecodings(self, s: str) -> int:
        curr = two_back = 0
        one_back = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            elif i < len(s) - 1 and (s[i] == "1" or s[i] == "2" and s[i+1] < "7"):
                curr = one_back
                curr += two_back
            else:
                curr = one_back
            
            curr, one_back, two_back = 0, curr, one_back
        return one_back
