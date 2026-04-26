class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def decision(opens, closes):
            if opens == closes == n:
                res.append("".join(curr))
            else:
                if opens < n:
                    curr.append("(")
                    decision(opens+1, closes)
                    curr.pop()

                if closes < opens:
                    curr.append(")")
                    decision(opens, closes+1)
                    curr.pop()

        decision(0, 0)
        return res
