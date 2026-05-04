class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        MAPPINGS = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        res = []
        comb = []

        def combs(i):
            if i == len(digits):
                res.append("".join(comb))
            else:
                for c in MAPPINGS[int(digits[i])]:
                    comb.append(c)
                    combs(i+1)
                    comb.pop()
        
        combs(0)
        return res
