import sys
import numpy as np

intToPlayer = {0: ' ', 1: 'X', 2: 'O'}

def main():
    sys.stdout.write("Let's play tic-tac-toe!\n")
    game()

def game():
    board = np.zeros((3, 3), dtype=int)
    hasWon = isWinScenario(board)
    while not hasWon:
        turn(1, board)
        print_board(board);
        hasWon = isWinScenario(board)
    sys.stdout.write("Congratulations!\n")

def turn(player, board):
    row = input("What row would you like to play? ")
    col = input("What column would you like to play? ")
    board[row][col] = player

def isWinScenario(board):
    for i in range(2):
        if isRowWin(board[i]):
            return True
        col = [row[i] for row in board]
        if isRowWin(col):
            return True
    for diag in [np.diag(board), np.diag(np.fliplr(board))]:
        if isRowWin(diag):
            return True
    return False

def isRowWin(row):
    return all(x == row[0] and x != 0 for x in row)

def print_board(board):
    text_board = "";
    for i in range(3):
        for j in range(3):
            suffix = "|" if j != 2 else ""
            char = intToPlayer[board[i][j]]
            text_board += char + suffix
        text_board += "\n"
        if i != 2:
            text_board += "_ _ _\n"
    sys.stdout.write(text_board)

if __name__ == "__main__":
    main()
