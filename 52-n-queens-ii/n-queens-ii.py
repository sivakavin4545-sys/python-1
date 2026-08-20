class Solution:
    def totalNQueens(self, n):
        def solve(row, cols, diagonals, anti_diagonals):
            if row == n:
                return 1

            count = 0

            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col

                if col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)

                count += solve(row + 1, cols, diagonals, anti_diagonals)

                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)

            return count

        return solve(0, set(), set(), set())