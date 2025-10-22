class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        def backtrack(r):
            # base case: all queens placed
            if r == n:
                # convert board to string representation
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # try placing a queen in every column of the current row
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # place queen
                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                # move to next row
                backtrack(r + 1)

                # backtrack (remove queen)
                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return res


# Example Test
solver = Solution()
solutions = solver.solveNQueens(4)

# Display solutions
for sol in solutions:
    for row in sol:
        print(row)
    print()
