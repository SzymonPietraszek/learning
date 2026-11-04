# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.


# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


# Constraints:


# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = nums[0] + nums[1] + nums[2]
        best_score = abs(target - best)
        prev_i_val = None
        for i in range(len(nums) - 2):
            i_val = nums[i]
            if prev_i_val == i_val:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                l_val, r_val = nums[l], nums[r]
                new_best = i_val + l_val + r_val
                new_best_score = abs(target - new_best)
                if new_best_score < best_score:
                    best_score = new_best_score
                    best = new_best
                    if best_score == 0:
                        return best
                if new_best < target:
                    l += 1
                    while l < r and nums[l] == l_val:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == r_val:
                        r -= 1
            prev_i_val = i_val
        return best


s = Solution()

print(s.threeSumClosest([-1, 2, 1, -4], 1))
print(s.threeSumClosest([0, 0, 0], 1))
