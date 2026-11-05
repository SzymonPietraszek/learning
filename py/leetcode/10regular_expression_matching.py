# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# Return a boolean indicating whether the matching covers the entire input string (not partial).


# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".


# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pi = 0
        for si in range(len(s)):
            if pi + 1 < len(p) and p[pi + 1] == "*":
                while pi + 3 < len(p) and p[pi + 3] == "*" and p[pi] == p[pi + 2]:
                    pi += 2
                while si < len(s) and p[pi] in [s[si], "."]:
                    if self.isMatch(s[si:], p[pi + 2 :]):
                        return True
                    si += 1
                return self.isMatch(s[si:], p[pi + 2 :])
            if pi < len(p) and p[pi] in [s[si], "."]:
                pi += 1
                continue
            return False
        while pi + 1 < len(p) and p[pi + 1] == "*":
            pi += 2
        return pi == len(p)


s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("ab", ".*"))
