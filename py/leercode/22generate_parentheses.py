# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = ["("]

        for i in range(2 * n - 1):
            new_ret = []
            for r in ret:
                o = r.count("(")
                if o < n:
                    new_ret.append(r + "(")
                if len(r) - o < o:
                    new_ret.append(r + ")")
            ret = new_ret

        return ret


s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
