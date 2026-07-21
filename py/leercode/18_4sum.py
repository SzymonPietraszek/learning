# 18. 4Sum
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()
        a_val_prev = None
        for a in range(len(nums) - 3):
            a_val = nums[a]
            if 4 * a_val > target:  # target can't be reached
                break
            if a_val == a_val_prev:
                continue
            a_val_prev = a_val

            b_val_prev = None
            for b in range(a + 1, len(nums) - 2):
                b_val = nums[b]
                if a_val + 3 * b_val > target:  # target can't be reached
                    break
                if b_val == b_val_prev:
                    continue
                b_val_prev = b_val

                s_ab = a_val + b_val
                l, r = b + 1, len(nums) - 1
                while l < r:
                    l_val, r_val = nums[l], nums[r]
                    if s_ab + 2 * l_val > target:  # target can't be reached
                        break
                    if s_ab + 2 * r_val < target:  # target can't be reached
                        break
                    s = s_ab + l_val + r_val
                    if s == target:
                        ret.append([a_val, b_val, l_val, r_val])
                    if s <= target:
                        l += 1
                        while nums[l] == l_val and l < r:
                            l += 1
                    if s >= target:
                        r -= 1
                        while nums[r] == r_val and l < r:
                            r -= 1
        return ret


s = Solution()

print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([2, 2, 2, 2, 2], 8))
