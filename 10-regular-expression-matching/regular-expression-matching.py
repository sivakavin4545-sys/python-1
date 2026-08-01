class Solution:
    def isMatch(self, s, p):
        memo = {}

        def match(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                result = match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                result = first_match and match(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return match(0, 0)