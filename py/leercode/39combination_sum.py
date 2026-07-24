# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []


# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ret = []
        less = []
        candidates.sort()

        prev = None
        for i, c in enumerate(candidates):
            if c == prev:
                continue
            if c < target:
                less.append([c])
            elif c == target:
                ret.append([c])
                candidates = candidates[:i]
            else:
                candidates = candidates[:i]
            prev = c

        candidates.remove(c)

        while less:
            less_plus_1 = []
            for l in less:
                last = l[-1]
                sl = sum(l)
                for c in candidates:
                    if c < last:
                        continue
                    if sl + c < target:
                        less_plus_1.append(l + [c])
                    elif sl + c == target:
                        ret.append(l + [c])
                    else:
                        break
            less = less_plus_1

        return ret


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2], 1))
