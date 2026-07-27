# 43. Multiply Strings
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"


# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ret = ""
        if num1 == "0" or num2 == "0":
            return "0"

        zeros = 0
        for d1 in num1[::-1]:
            if d1 == "0":
                zeros += 1
                continue

            res = 0
            v = ret[len(ret) - zeros :]
            v = "0" * (zeros - len(v)) + v
            for i in range(len(num2)):
                m = int(d1) * int(num2[len(num2) - 1 - i]) + res
                ret_i = len(ret) - 1 - i - zeros
                if ret_i >= 0:
                    m += int(ret[ret_i])
                res = m // 10
                v = str(m % 10) + v
            if res:
                v = str(res) + v
            ret = v
            zeros += 1
        return ret


s = Solution()
print(s.multiply("2", "3"))
print(s.multiply("123", "456"))
