# 6. Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);


# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"


# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000


class Solution:
    # 3
    # 0 4 8 12 PAHN
    # 1 3 5 7 9 11 APLSIIG
    # 2 6 10 YIR

    # 4
    # 0 6 12
    # 1 5 7 11 13
    # 2 4 8 10
    # 3 9
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ret = []
        m = 2 * (numRows - 1)

        for i in range(numRows):
            for j in range(i, len(s), m):
                ret.append(s[j])
                if i % (numRows - 1) == 0:
                    continue
                k = j + m - 2 * i
                if k < len(s):
                    ret.append(s[k])

        return "".join(ret)


s = Solution()
print(s.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(s.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(s.convert("A", 1))  # Output: "A"
print(s.convert("", 1))  # Output: ""
print(s.convert("", 5))  # Output: ""
