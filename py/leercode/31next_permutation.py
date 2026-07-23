# 31. Next Permutation
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.


# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]


# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                found = i - 1
                break

        l, r = found + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        for i in range(found + 1, len(nums)):
            if nums[i] > nums[found]:
                nums[i], nums[found] = nums[found], nums[i]
                break


s = Solution()
for nums in [
    [1, 2, 3],
    [3, 2, 1],
    [1, 1, 5],
    [1, 2, 4, 3],
    [1, 5, 6, 5, 4, 3],
]:
    print("------------------")
    print(nums)
    s.nextPermutation(nums)
    print(nums)

# 1 5 6 5 4 3
# 1 5|3 4 5 6


# 8 9 7 5 3 1
# 1 9 7 5 3 9
# 1 3 7 5 7 9
# 1 3 5 5 7 9
# 1 3 8 5 7 9

# 6 9 7 5 3 1
# 1         9
# 1 3     7 9
# 1 3     7 9
