# 45. Jump Game II
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2


# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].


class Solution:
    def jump(self, nums: List[int]) -> int:
        best = []
        best_pos = 0
        next_best = -1
        next_best_pos = 0
        for i in range(len(nums)):
            if i > best_pos:
                best.append(next_best)
                best_pos = next_best_pos
            score = i + nums[i]
            if score > next_best_pos:
                next_best = i
                next_best_pos = score

        return len(best)


s = Solution()

print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 0, 1, 4]))
print(s.jump([3, 4, 3, 2, 5, 4, 3]))
print(s.jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]))
