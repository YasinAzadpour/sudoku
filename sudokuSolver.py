import numpy as np


class Sudoku:

    def __init__(self, board):
        assert board.shape == (9, 9)
        assert type(board) == np.ndarray
        self.board = board

    def _roundup_to_nearest_three(self, index):
        return int(np.ceil((index + 1) / 3) * 3)

    def _check_unique(self, row, column):
        # Get distinct values from row and column
        row_values = np.unique(self.board[row,:])
        col_values = np.unique(self.board[:,column])
        
        # First define the sub cell that the row/column falls into
        # This will be a group of 3 in each axis
        row_end_pos = self._roundup_to_nearest_three(row)
        col_end_pos = self._roundup_to_nearest_three(column)
        
        # Then get distinct values from sub cells
        box_values = np.unique(self.board[row_end_pos-3:row_end_pos, 
                                    col_end_pos-3:col_end_pos])
        
        # Bring all into one list
        all_values = np.concatenate((row_values, col_values, box_values), axis=None)
        
        # Then take the unique values from all of them
        unique_values = np.unique(all_values)
        
        return unique_values

    def _fill_values(self, row, column):
        # We're only interested in values not yet filled
        if self.board[row,column] == 0:
            existing_values = self._check_unique(row, column)
            potential_values = [value for value in range(1,10) if value not in existing_values]
            
            # If there's only one potential solution, overwrite zero with that value
            if len(potential_values) == 1:
                self.board[row,column] = potential_values[0]

    def solve(self):
        zeroes_remaining = 81
        count = 0
        while zeroes_remaining != 0:
            if count>=10:
                return False
            
            # Loop through table columns & rows
            for row in range(9):
                for column in range(9):
                    self._fill_values(row, column)
                    
            # Checks array for number of non-filled values remaining
            count += 1
            zeroes_remaining = np.count_nonzero(self.board == 0)
            
        return True

    def show_board(self):
        output = ""
        board = self.board.astype(str)
        for i in range(9):
            
            if i % 3 == 0:
                output += '\n'

            row = board[i]

            output += f"{' '.join(row[0:3])}  {' '.join(row[3:6])}  {' '.join(row[6:])}\n"
        
        output = output.strip()
        return output




if __name__ == '__main__':
	
	# sample sudoku
    board_init = np.array([
    	[0,7,0,  2,3,8,  0,0,0], 
    	[0,0,0,  7,4,0,  8,0,9], 
    	[0,6,8,  1,0,9,  0,0,2], 
        
    	[0,3,5,  4,0,0,  0,0,8], 
    	[6,0,7,  8,0,2,  5,0,1], 
    	[8,0,0,  0,0,5,  7,6,0], 

    	[2,0,0,  6,0,3,  1,9,0], 
    	[7,0,9,  0,2,1,  0,0,0], 
    	[0,0,0,  9,7,4,  0,8,0],
    ], dtype=int)

    sudoku = Sudoku(board_init)
    sudoku.solve()
    print("sample sudoku solve\n")
    print(sudoku.show_board())
    

