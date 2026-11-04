# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(lambda: -1)
        m = l = r = 0
        while r < len(s):
            prev = seen[s[r]]
            if prev >= l:
                l = prev + 1
            seen[s[r]] = r

            m = max(m, r - l + 1)
            r += 1
        return m


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
