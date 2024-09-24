import time
import tkinter as tk


def find_next_empty(puzzle):
    # find unfilled space
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None


def is_valid(puzzle, guess, row, col):
    # determines if guess valid
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # col_vals = []
    # for i in range(9):
    #   col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def sudoku_solver(puzzle):
    # puzzle is list of list
    # Find somewheree to put a guess
    row, col = find_next_empty(puzzle)
    # If no remaining spaces we're done
    if row is None:
        return True
    # if space open
    for guess in range(1, 10):
        # check if valid
        if is_valid(puzzle, guess, row, col):
            # if valid make guess
            puzzle[row][col] = guess
            if sudoku_solver(puzzle):
                return True
        # If not valid or didn't solve the puzzle
        puzzle[row][col] = 0  # reset guess
    # if no numbers work it is unsolveable
    return False


def make_str(row, board):
    board_row = ''
    for num in range(9):
        if num == 3 or num == 6:
            board_row += f'  |  {board[row][num]} '
        else:
            board_row += f' {board[row][num]} '
    return board_row


def main():
    start_time = time.time()
    board = [
        [3, 9, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 5],
        [0, 0, 0, 7, 1, 9, 0, 8, 0],

        [0, 5, 0, 0, 6, 8, 0, 0, 0],
        [2, 0, 6, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],

        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 7, 0, 1, 0, 5, 0, 4, 0],
        [1, 0, 9, 0, 0, 0, 2, 0, 0]
    ]
    sudoku_solver(board)
    end_time = time.time()
    window = tk.Tk()
    # window.geometry("300x300")
    window.title('Sudoku Solver')
    window.config(bg='black')

    boardr1 = make_str(0, board)
    boardr2 = make_str(1, board)
    boardr3 = make_str(2, board)
    boardr4 = make_str(3, board)
    boardr5 = make_str(4, board)
    boardr6 = make_str(5, board)
    boardr7 = make_str(6, board)
    boardr8 = make_str(7, board)
    boardr9 = make_str(8, board)

    labelv = tk.Label(text=f'This board is valid: {sudoku_solver(board)}', height=3, bg='black', fg='yellow')
    label1 = tk.Label(text=f'{boardr1}', bg='black', fg='yellow')
    label2 = tk.Label(text=f'{boardr2}', bg='black', fg='yellow')
    label3 = tk.Label(text=f'{boardr3}', bg='black', fg='yellow')
    buffer1 = tk.Label(text=f'----------  -----------   ---------', bg='black', fg='yellow')
    label4 = tk.Label(text=f'{boardr4}', bg='black', fg='yellow')
    label5 = tk.Label(text=f'{boardr5}', bg='black', fg='yellow')
    label6 = tk.Label(text=f'{boardr6}', bg='black', fg='yellow')
    buffer2 = tk.Label(text=f'----------   -----------   ---------', bg='black', fg='yellow')
    label7 = tk.Label(text=f'{boardr7}', bg='black', fg='yellow')
    label8 = tk.Label(text=f'{boardr8}', bg='black', fg='yellow')
    label9 = tk.Label(text=f'{boardr9}', bg='black', fg='yellow')
    labelt = tk.Label(text=f'Time: {end_time - start_time}', height=3, bg='black', fg='yellow')

    labelv.grid(column=0, row=0)
    label1.grid(column=0, row=1)
    label2.grid(column=0, row=2)
    label3.grid(column=0, row=3)
    buffer1.grid(column=0, row=4)
    label4.grid(column=0, row=5)
    label5.grid(column=0, row=6)
    label6.grid(column=0, row=7)
    buffer2.grid(column=0, row=8)
    label7.grid(column=0, row=9)
    label8.grid(column=0, row=10)
    label9.grid(column=0, row=11)
    labelt.grid(column=0, row=12)

    window.mainloop()


if __name__ == '__main__':
    main()
