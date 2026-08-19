# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        t = (len(a) + len(b)) // 2
        even = (len(a) + len(b)) % 2 == 0
        if even:
            t -= 1

        ai = bi = -1
        n1 = n2 = None
        while True:
            if ai == len(a) - 1:
                bi = t - ai - 2
                n1, n2 = b[bi + 1], b[bi + 2] if even else None
                break
            elif bi == len(b) - 1:
                ai = t - bi - 2
                n1, n2 = a[ai + 1], a[ai + 2] if even else None
                break
            step = (t - (ai + bi + 2) + 1) // 2
            if step == 0:
                break
            next_ai = min(ai + step, len(a) - 1)
            next_bi = min(bi + step, len(b) - 1)
            if a[next_ai] <= b[next_bi]:
                ai = next_ai
            else:
                bi = next_bi

        if n1 is None:
            n1 = min(a[ai + 1], b[bi + 1])
            if even and a[ai + 1] <= b[bi + 1]:
                n2 = b[bi + 1]
                if ai + 2 < len(a) and a[ai + 2] < n2:
                    n2 = a[ai + 2]
            elif even:
                n2 = a[ai + 1]
                if bi + 2 < len(b) and b[bi + 2] < n2:
                    n2 = b[bi + 2]

        return (n1 + n2) / 2 if n2 else n1


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
print(s.findMedianSortedArrays([1, 2], [3, 4, 5]))
