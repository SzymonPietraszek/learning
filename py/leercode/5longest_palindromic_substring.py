# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"


# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        ret = ""
        ret_max = 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return l + 1, r - 1

        def update_max(l, r):
            nonlocal s, ret, ret_max
            new_max = r + 1 - l
            if ret_max < new_max:
                ret = s[l : r + 1]
                ret_max = new_max

        for m in range(len(s)):
            update_max(*expand(m - 1, m + 1))  # _ _ x _ _
            update_max(*expand(m, m + 1))  # _ _ x x _ _
        return ret


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome(""))
