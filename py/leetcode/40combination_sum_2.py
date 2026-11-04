# 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]


# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        curr = [0]
        s = candidates[0]
        i = 1
        while True:
            while i < len(candidates) and s < target:
                curr.append(i)
                s += candidates[i]
                i += 1

            if s == target:
                ret.append([candidates[j] for j in curr])
            if s >= target:
                s -= candidates[curr.pop()]

            if not curr:
                break

            prev = curr.pop()
            s -= candidates[prev]
            i = prev + 1
            while i < len(candidates) and candidates[i - 1] == candidates[i]:
                i += 1

        return ret


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(s.combinationSum2([2, 5, 2, 1, 2], 5))
