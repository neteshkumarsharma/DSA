class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        currentCandidates = []
        result = []
        def comb(startIndex, remaningSum):
            if remaningSum == 0:
                result.append(currentCandidates[:])
                return
            if remaningSum < candidates[startIndex]:
                return
            for index in range(startIndex, len(candidates)):
                currentCandidates.append(candidates[index])
                comb(index, remaningSum - candidates[index])
                currentCandidates.pop()
        comb(0, target)
        return result