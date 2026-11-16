class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        threes = rols = cols = True
        cols = True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                threes = threes and self.threeByThree(i, i + 3, j, j + 3, board)
                if threes == False:
                    return False
        
        for j in range(9):
            cols = self.col(j, board)
            if cols == False:
                return False

        for i in range(9):
            rows = self.row(i, board)
            if rows == False:
                return False

        return (threes and rows and cols)
        
    def threeByThree(self, start: int, end: int, start2: int, end2: int, board: List[List[str]]) -> bool:
        nums = set()
        for i in range(start, end, 1):
            for j in range(start2, end2, 1):
                if board[i][j] in nums:
                    return False
                elif board[i][j] == ".":
                    continue
                else:
                    nums.add(board[i][j])
        return True

    def col(self, j: int, board: List[List[str]]) -> bool:
        nums = set()
        for i in range(9):
            if board[i][j] in nums:
                return False
            elif board[i][j] == ".":
                continue
            else:
                nums.add(board[i][j])
        return True

    def row(self, i: int, board: List[List[str]]) -> bool:
        nums = set()
        for j in range(9):
            if board[i][j] in nums:
                return False
            elif board[i][j] == ".":
                continue
            else:
                nums.add(board[i][j])
        return True
