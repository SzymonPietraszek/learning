# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


# Constraints:

# -231 <= x <= 231 - 1


def itol(x):
    if x == 0:
        return [0]
    ret = []
    while x > 0:
        ret.append(x % 10)
        x //= 10
    return ret


def ltoi_rev(l):
    x = 0
    for i in l:
        x *= 10
        x += i
    return x


max32 = itol(2**31 - 1)
max32.reverse()
min32 = itol(2**31)
min32.reverse()


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = sign * x
        xl = itol(x)
        m = max32 if sign == 1 else min32
        if len(xl) == len(m):
            for i in range(len(xl)):
                if xl[i] > m[i]:
                    return 0
                elif xl[i] < m[i]:
                    break
        return sign * ltoi_rev(xl)


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(-(2**32) - 2))
print(s.reverse(8463847412))
print(s.reverse(7463847412))
print(s.reverse(-8463847412))
print(s.reverse(-9463847412))
