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

        l, r = 0, len(nums) - 1
        pivot = l if nums[l] == target else r if nums[r] == target else -1
        while pivot < 0 and l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                pivot = m
                break
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if pivot == -1:
            return [-1, -1]
        ll, rr = l, r
        l, r = ll, pivot
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target and (m == 0 or nums[m - 1] != target):
                ll = m
                break
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        l, r = pivot, rr
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target and (m == len(nums) - 1 or nums[m + 1] != target):
                rr = m
                break
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [ll, rr]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
print(s.searchRange([], 0))
print(s.searchRange([1], 1))
print(s.searchRange([1, 1], 1))
print(s.searchRange([1, 2, 1], 1))
