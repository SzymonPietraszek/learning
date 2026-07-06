# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        ll = -1
        l, r = 0, len(nums) - 1
        rr = r
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] >= target:
                if nums[m] == target:
                    ll = m
                else:
                    rr = m
                r = m - 1

        if ll == -1:
            return [-1, -1]

        l, r = ll, rr
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                rr = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1

        return [ll, rr]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
print(s.searchRange([], 0))
print(s.searchRange([1], 1))
print(s.searchRange([1, 1], 1))
print(s.searchRange([1, 2, 1], 1))
