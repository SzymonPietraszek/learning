class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        c = strs[0]

        for s in strs[1:]:
            while True:
                if not c:
                    return ""
                if s.startswith(c):
                    break
                c = c[:-1]

        return c
