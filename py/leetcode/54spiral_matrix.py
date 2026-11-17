# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.


# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ret = []
        m = len(matrix)
        n = len(matrix[0])
        i, j, d = 0, 0, 0
        up, down, left, right = 1, m - 1, 0, n - 1
        while len(ret) < m * n:
            ret.append(matrix[i][j])
            if d % 4 == 0 and j < right:
                j += 1
            elif d % 4 == 0:
                right, d, i = right - 1, d + 1, i + 1
            elif d % 4 == 1 and i < down:
                i += 1
            elif d % 4 == 1:
                down, d, j = down - 1, d + 1, j - 1
            elif d % 4 == 2 and j > left:
                j -= 1
            elif d % 4 == 2:
                left, d, i = left + 1, d + 1, i - 1
            elif d % 4 == 3 and i > up:
                i -= 1
            elif d % 4 == 3:
                up, d, j = up + 1, d + 1, j + 1

        return ret


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
