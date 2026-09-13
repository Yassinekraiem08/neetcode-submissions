class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack (row, column, i):
            if i == len(word):
                return True
                
            if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]):
                return False
            
            if board[row][column] != word[i]:
                return False
            
            letter = board[row][column]
            board[row][column] = "#"

            found = (backtrack(row + 1, column, i + 1) or backtrack(row - 1, column, i + 1) or backtrack(row, column - 1, i+1) or backtrack(row, column + 1, i + 1))
            
            board[row][column] = letter
            return found
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if backtrack(row, column, 0):
                    return True

        return False
            
