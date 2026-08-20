class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add an opening bracket if available
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # A closing bracket is valid only after an opening bracket
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result