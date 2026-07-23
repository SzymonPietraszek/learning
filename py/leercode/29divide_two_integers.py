# 29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.


# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.


# Constraints:

# -231 <= dividend, divisor <= 231 - 1
# divisor != 0


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        sign1 = "-" if dividend < 0 else ""
        dividend_s = str(dividend).removeprefix(sign1)

        sign2 = "-" if divisor < 0 else ""
        divisor_s = str(divisor).removeprefix(sign2)
        divisor = int(divisor_s)

        ret = sign1 + sign2
        if len(ret) == 2:
            ret = ""

        if divisor < 10:
            val = 0
        else:
            val = int(dividend_s[0 : len(divisor_s) - 1])
        for c in dividend_s[len(divisor_s) - 1 :]:
            val = int(str(val) + c)
            j = 0
            while val >= divisor:
                val -= divisor
                j += 1
            ret += str(j)

        if ret == "-" or ret == "":
            return 0
        return int(ret)

    # 1234567 / 4321
    # 1234 / 4321 * 1000 +
    # xxxx / yyyy * 100
    # 1036963541 / 24409858
    # 24409858
    #  97639432   4
    #   60569221


s = Solution()

print(s.divide(10, 3))
print(s.divide(7, -3))
print(s.divide(1036963541, -24409858))
