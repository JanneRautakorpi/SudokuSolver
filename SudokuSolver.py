board = [
    [5, 4, 0, 0, 0, 0, 0, 0, 0],
    [8, 3, 0, 2, 0, 0, 0, 0, 0],
    [6, 7, 2, 0, 8, 4, 1, 0, 0],
    [0, 5, 7, 0, 3, 0, 6, 0, 0],
    [0, 8, 0, 1, 9, 0, 0, 5, 0],
    [3, 9, 0, 0, 4, 5, 0, 0, 2],
    [0, 1, 5, 0, 0, 0, 0, 6, 0],
    [0, 6, 0, 4, 2, 9, 0, 0, 1],
    [0, 2, 0, 0, 6, 0, 4, 0, 0]
]

def printBoard(board):
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if j == 2 or j == 5:
                print(num, end="|")
            else:
                print(num, end=" ")
        if i == 2 or i == 5:
            print()
            print("-"*18)
        else:
            print()

def findUnsolved(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                return (i, j) 

    return None, None

def isValid(board, row, col, number):
    for i in range(len(board)):
        if (board[row][i] == number
            or board[i][col] == number):
            return False
    
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == number:
                return False
    return True

def solve(board):
    row, col = findUnsolved(board)
    if (row == None and col == None):
        # Board is solved
        return True
    
    for number in range(1, 10):
        if isValid(board, row, col, number):
            board[row][col] = number

            # Check if board is now solved. If it is,
            # return True
            if (solve(board)):
                return True
            board[row][col] = 0
    
def main():
    solve(board)
    printBoard(board)

if __name__ == "__main__":
    main()
