class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, comb = [], []
        candidates.sort()

        def backtrack(idx):
            print(idx, comb)
            if sum(comb) == target:
                res.append(comb[:])
            if sum(comb) >= target or idx >= len(candidates):
                return
            comb.append(candidates[idx])
            backtrack(idx+1)
            comb.pop()
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(idx+1)
        
        backtrack(0)
        return res
