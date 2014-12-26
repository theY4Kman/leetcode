class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        board = [[int(c) if c.isdigit() else None for c in r] for r in board]

        for row in board:
            nums = set()
            for n in row:
                if n:
                    if n in nums:
                        return False
                    nums.add(n)

        for y in xrange(len(board)):
            nums = set()
            for x in xrange(len(board)):
                n = board[x][y]
                if n:
                    if n in nums:
                        return False
                    nums.add(n)

        for o_x in xrange(0, len(board), 3):
            for o_y in xrange(0, len(board), 3):
                nums = set()
                for x in xrange(3):
                    for y in xrange(3):
                        n = board[o_x + x][o_y + y]
                        if n:
                            if n in nums:
                                return False
                            nums.add(n)

        return True

    tests = [
        ([".87654321",
          "2........",
          "3........",
          "4........",
          "5........",
          "6........",
          "7........",
          "8........",
          "9........"],
            True),
        (["..4...63.",
          ".........",
          "5......9.",
          "...56....",
          "4.3.....1",
          "...7.....",
          "...5.....",
          ".........",
          "........."],
         False)
    ]
