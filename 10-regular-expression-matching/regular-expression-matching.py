class Solution:
    def isMatch(self, s, p):
        memo = {}

        def dp(i, j):
            # Have we already solved this state?
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern is finished: string must also be finished
            if j == len(p):
                return i == len(s)

            # Does current pattern character match current string character?
            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == ".")
            )

            # Next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == "*":
                result = (
                    dp(i, j + 2) or              # Use zero occurrences
                    (first_match and dp(i + 1, j)) # Use one or more
                )
            else:
                result = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dp(0, 0)