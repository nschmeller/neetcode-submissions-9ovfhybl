from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comb, res = [], []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(list(comb))
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                elif total + candidates[i] > target:
                    break
                else:
                    comb.append(candidates[j])
                    backtrack(j+1, total + candidates[j])
                    comb.pop()

        backtrack(0, 0)
        return res
