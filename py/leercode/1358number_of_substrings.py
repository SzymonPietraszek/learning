# 1358. Number of Substrings Containing All Three Characters
# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.


# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
# Example 3:

# Input: s = "abc"
# Output: 1


from collections import defaultdict


class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        req = set(["a", "b", "c"])
        count = 0
        c = defaultdict(int)
        start = 0
        end = 2
        c[s[0]] += 1
        c[s[1]] += 1
        while end < len(s):
            c[s[end]] += 1
            while c["a"] > 0 and c["b"] > 0 and c["c"] > 0:
                count += len(s) - end
                c[s[start]] -= 1
                start += 1
            end += 1


s = Solution()

print(s.numberOfSubstrings("abcabc"))
print(s.numberOfSubstrings("aaacb"))
print(s.numberOfSubstrings("abc"))
print(
    s.numberOfSubstrings(
        "bbaaababaacabccabcaacbbbacababcbbcbaccbbabaabbbbabaaabbbacbccacbcaccabbcbccacbaaaaaacbacbabbcccbacaabacacbacacaaaacbabccacbccaaacacaabcaacaacbbcacabaacaccbabcccbbccbbbbbabbcacbcbbbbcabbaabbbabbbcacbaabaaaabacbcbbcccbcaabcccabcaccabbbcbaabacccbbaccaccccbbccacaabccccbcbbcbbbbbbcbacacbbccbaccabcaabbbccbcbcccaaaabbacccbaaccacbabbcaaccbaacaaabaccaaabcacabccabaccbacaaaababbbacbcccabcacbcccbabcacbbbacacbbabaacbcbccccbbccccacccacbabaacbcccabbcbaccaaccaabccccccacccccbcabbccbbbabaacaacccbabababaacaabacccbccbcaccbbbaccccabccaacacbacabccbbbbacacbcccbbaaacbaaaccaaacacbacabcacacbabcbabacbcbcbbbaaabcaaabbcbbcbbccaabbbaacaacccbccaaacccbcbacbaaabaabccbcacbacaabbccacaabbbbabbaccacacaaaababccbaccaccaccacabbaabbbbbababcbcccbaaacaccabbabb"
    )
)
