from random import randint

def printBoard(gameBoard: list, position: int, char: str) -> None:
    """
    Updates the Tic Tac Toe board with the latest move and prints the updated board.

    Args:
        gameBoard (list): Represents the current state of the Tic Tac Toe board.
        position (int): The position where the player's move is placed.
        char (str): The character ('X' or 'O') placed in the position.
        
    Returns:
        None
    """
    gameBoard[position] = char
    
    # Display the updated board with 'X' or 'O' in the chosen position
    print(f" {gameBoard[0]} | {gameBoard[1]} | {gameBoard[2]} ")
    print("-----------")
    print(f" {gameBoard[3]} | {gameBoard[4]} | {gameBoard[5]} ")
    print("-----------")
    print(f" {gameBoard[6]} | {gameBoard[7]} | {gameBoard[8]} ")


def checkWinnerByRow(gameBoard: list, rowNumber: int, char: str) -> bool:
    """
    Checks for a win condition in a specific row of the Tic Tac Toe board.

    Args:
        gameBoard (list): Represents the current state of the Tic Tac Toe board.
        rowNumber (int): The row number to check for a win (1, 2, or 3).
        char (str): The character ('X' or 'O') to check for in the row.

    Returns:
        bool: True if the specified row contains all 'char', False otherwise.
    """
    # Checks each row for a win condition based on the character ('X' or 'O')
    if rowNumber == 1:
        # Checks the first row
        for i in range(3):
            if gameBoard[i] != char:
                return False
        return True
    elif rowNumber == 2:
        # Checks the second row
        for i in range(3, 6):
            if gameBoard[i] != char:
                return False
        return True
    else:
        # Checks the third row
        for i in range(6, 9):
            if gameBoard[i] != char:
                return False
        return True


def checkWinnerByDiagonal(gameBoard: list, diagonalNumber: int, char: str) -> bool:
    """
    Checks for a win condition in a diagonal of the Tic Tac Toe board.

    Args:
        gameBoard (list): Represents the current state of the Tic Tac Toe board.
        diagonalNumber (int): The diagonal number to check (1 or 2).
        char (str): The character ('X' or 'O') to check for in the diagonal.

    Returns:
        bool: True if the specified diagonal contains all 'char', False otherwise.
    """
    # Checks for a win condition in the diagonals based on the character ('X' or 'O')
    if diagonalNumber == 1:
        # Checks the main diagonal (top-left to bottom-right)
        if gameBoard[0] == gameBoard[4] == gameBoard[8] == char:
            return True
        return False
    else:
        # Checks the secondary diagonal (top-right to bottom-left)
        if gameBoard[2] == gameBoard[4] == gameBoard[6] == char:
            return True
        return False


def checkWinnerByColumn(gameBoard: list, columnNumber: int, char: str) -> bool:
    """
    Checks for a win condition in a specific column of the Tic Tac Toe board.

    Args:
        gameBoard (list): Represents the current state of the Tic Tac Toe board.
        columnNumber (int): The column number to check for a win (1, 2, or 3).
        char (str): The character ('X' or 'O') to check for in the column.

    Returns:
        bool: True if the specified column contains all 'char', False otherwise.
    """
    # Checks for a win condition in the columns based on the character ('X' or 'O')
    if columnNumber == 1:
        # Checks the first column
        if gameBoard[0] == gameBoard[3] == gameBoard[6] == char:
            return True
        return False
    elif columnNumber == 2:
        # Checks the second column
        if gameBoard[1] == gameBoard[4] == gameBoard[7] == char:
            return True
        return False
    else:
        # Checks the third column
        if gameBoard[2] == gameBoard[5] == gameBoard[8] == char:
            return True
        return False


def main() -> None:
    """
    Manages the execution of the Tic Tac Toe game.

    This function orchestrates the gameplay of Tic Tac Toe between the user (as 'X') 
    and the computer (as 'O'). It initializes the game board, accepts user inputs, 
    validates moves, checks for a win or tie, and handles the computer's moves.

    Returns:
        None

    Raises:
        IndexError: If the user inputs an invalid board position (not within 0-8).
        Exception: Any other unexpected exception during gameplay.

    Notes:
        - The gameBoard is represented as a list of length 9, initially filled with spaces (' ').
        - The counter keeps track of the number of moves played to determine game progress.
        - It utilizes the 'printBoard', 'checkWinnerByRow', 'checkWinnerByDiagonal', and 'checkWinnerByColumn' 
          functions to assess win conditions and update the game state.

    Workflow:
        1. Displays the game instructions and the initial board layout.
        2. Manages the game loop:
            a. Receives the user's desired position and validates it.
            b. Updates the board according to the user's move ('X').
            c. Checks for a win or tie after each move.
            d. Simulates the computer's move ('O') if the game is still in progress.
            e. Repeats steps a-d until the game concludes.
        3. Prints the game outcome - whether a player wins or it's a tie.
    
    Internal Logic:
        - Prompts the user for a move and validates the input position.
        - Checks if the chosen position is available; if so, updates the board.
        - Checks for a win or tie condition after each player's move.
        - Handles the computer's move by selecting an available position randomly.
        - Continues gameplay until a win, tie, or the board is full (9 moves).

    Examples:
        >>> main()  # Initiates the Tic Tac Toe game.
    """
    # The initial setup of the game with an empty board, counter for moves, and printing the initial layout
    print("\n\t\tTIC-TAC-TOE!!\n\tUser plays as 'X', COM plays as 'O'", sep="")
    gameBoard = 9 * [' ']
    counter = 0
    print("\n\n")
    print("      0  | 1  | 2   ")
    print("     ____|____|____ ")
    print("      3  | 4  | 5    ")
    print("     ____|____|____ ")
    print("      6  | 7  | 8     ")
    print("         |    |      \n")

    # Game loop runs until a win, tie, or maximum moves (9) are reached
    while counter < 9:
        while True:
            try:
                # Accepts user input for the desired position and validates it
                userPosition = int(input("\nEnter a position from 0-8: "))
                if gameBoard[userPosition] == ' ':
                    # Updates the board and increments the move counter for the user's move
                    printBoard(gameBoard, userPosition, 'X')
                    counter += 1
                    break
                else:
                    # Informs the user if the selected position is already taken and prompts for a new input
                    print(f"\nPosition contains {gameBoard[userPosition]}, try again")
                    continue
            except IndexError:
                # Handles exceptions when the user inputs an invalid position
                print("\nPosition out of Board range, Try again with a valid position.")
            except Exception as ex:
                # Catches any unexpected exceptions during gameplay
                print()
                print(ex)

        # Checks for a win or tie condition after the user's move
        if counter >= 5:
            if checkWinnerByRow(gameBoard, 1, 'X') or checkWinnerByRow(gameBoard, 2, 'X') or checkWinnerByRow(gameBoard, 3, 'X'):
                print("\nPlayer 'X' WINS the game!!!")
                break
            elif checkWinnerByDiagonal(gameBoard, 1, 'X') or checkWinnerByDiagonal(gameBoard, 2, 'X'):
                print("\nPlayer 'X' WINS the game!!!")
                break
            elif checkWinnerByColumn(gameBoard, 1, 'X') or checkWinnerByColumn(gameBoard, 2, 'X') or checkWinnerByColumn(gameBoard, 3, 'X'):
                print("\nPlayer 'X' WINS the game!!!")
                break

        # Checks for a tie condition after the maximum moves (9) without a win
        if counter == 9:
            print("It's a TIE!!!")
            break

        # Simulates the computer's move ('O') if the game is still in progress
        print("\nCOM Plays: ")
        while True:
            COM = randint(0, 8)
            if gameBoard[COM] == ' ':
                # Updates the board and increments the move counter for the computer's move
                printBoard(gameBoard, COM, 'O')
                counter += 1
                break
            else:
                COM = randint(0, 8)

        # Checks for win conditions after the computer's move
        if counter >= 5:
            if checkWinnerByRow(gameBoard, 1, 'X') or checkWinnerByRow(gameBoard, 2, 'X') or checkWinnerByRow(gameBoard, 3, 'X'):
                print("\nPlayer 'X' WINS the game!!!")
                break
            elif checkWinnerByDiagonal(gameBoard, 1, 'X') or checkWinnerByDiagonal(gameBoard, 2, 'X'):
                print("\nPlayer 'X' WINS the game!!!")
                break
            elif checkWinnerByColumn(gameBoard, 1, 'X') or checkWinnerByColumn(gameBoard, 2, 'X') or checkWinnerByColumn(gameBoard, 3, 'X'):
                print("\nPlayer 'X' WINS the game!!!")
                break
            # Checks for the win conditions for 'O' after the computer's move
            elif checkWinnerByRow(gameBoard, 1, 'O') or checkWinnerByRow(gameBoard, 2, 'O') or checkWinnerByRow(gameBoard, 3, 'O'):
                print("\nPlayer 'O' WINS the game!!!")
                break
            elif checkWinnerByDiagonal(gameBoard, 1, 'O') or checkWinnerByDiagonal(gameBoard, 2, 'O'):
                print("\nPlayer 'O' WINS the game!!!")
                break
            elif checkWinnerByColumn(gameBoard, 1, 'O') or checkWinnerByColumn(gameBoard, 2, 'O') or checkWinnerByColumn(gameBoard, 3, 'O'):
                print("\nPlayer 'O' WINS the game!!!")
                break


if __name__ == "__main__":
    main()

