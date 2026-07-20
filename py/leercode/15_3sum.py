# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = []
        nums.sort()
        prev_i_val = None
        for i in range(len(nums) - 2):
            i_val = nums[i]
            if i_val > 0:
                break
            if prev_i_val == i_val:
                continue
            l, r = i + 1, len(nums) - 1
            target = -1 * i_val
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    ret.append([i_val, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
            prev_i_val = i_val

        return ret


s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0, 1, 1]))
print(s.threeSum([0, 0, 0]))
print(s.threeSum([1, 2, 0, 1, 0, 0, 0, 0]))
