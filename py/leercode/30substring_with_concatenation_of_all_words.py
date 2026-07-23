# 30. Substring with Concatenation of All Words
# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.


# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].


# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.

from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []

        sn = len(s)
        wn = len(words[0])
        n = len(words) * wn
        ws = defaultdict(int)
        for w in words:
            ws[w] += 1

        for offset in range(wn):
            for i in range(offset, sn - n + 1, wn):
                if i == offset:
                    sub = [s[i + j : i + j + wn] for j in range(0, n, wn)]
                    mws = ws.copy()
                    total = 0
                    for su in sub:
                        if su in mws:
                            mws[su] -= 1
                    for _, val in mws.items():
                        if val != 0:
                            total += 1
                    last = 0
                else:
                    prev = sub[last]
                    if prev in mws:
                        mws[prev] += 1
                        if mws[prev] == 0:
                            total -= 1
                        elif mws[prev] == 1:
                            total += 1

                    sub[last] = s[i + n - wn : i + n]
                    if sub[last] in mws:
                        mws[sub[last]] -= 1
                        if mws[sub[last]] == 0:
                            total -= 1
                        elif mws[sub[last]] == -1:
                            total += 1

                    last = (last + 1) % len(sub)

                if total == 0:
                    ret.append(i)

        return ret


s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))


# abcdefgh
# [ab, cd]

# [ab, cd] 0
# [cd, ef] 2
# [ef, gh] 4

# [bc, de] 1
# [de, fg] 3

# bar foo foo bar the foo bar man


# PREVIOUS WRONG BUT ALSO INTERESTING SOLUTION
#                 if i == offset:
#                     sub = [s[i + j: i + j + wn] for j in range(0, n, wn)]
#                     idxs = list(range(len(sub)))
#                     idxs.sort(key = lambda i: sub[i])
#                     last = 0
#                 else: # 1 3 5.    1 6 5
#                     prev = sub[last]
#                     sub[last] = s[i + n - wn: i + n]
#                     last_idx = idxs.index(last) # idxs[last_idx] == last
#                     if prev < sub[last]:
#                         for j in range(last_idx + 1, len(sub)):
#                             if sub[idxs[j - 1]] > sub[idxs[j]]:
#                                 idxs[j - 1], idxs[j] = idxs[j], idxs[j - 1]
#                             else:
#                                 break
#                     elif prev > sub[last]:
#                         for j in range(last_idx - 1, -1, -1):
#                             if sub[idxs[j + 1]] < sub[idxs[j]]:
#                                 idxs[j + 1], idxs[j] = idxs[j], idxs[j + 1]
#                             else:
#                                 break
#                     last += 1
#                     last %= len(sub)

#                 same = True
#                 for j, idx in enumerate(idxs):
#                     if sub[idx] != words[j]:
#                         same = False
#                         break

#                 if same:
#                     ret.append(i)
