import random

class TicTacToe:
    """
    A class to represent a Tic-Tac-Toe game.
    Can be played against a computer or another player.
    """

    def __init__(self) -> None:
        """
        Initializes the TicTacToe game.

        The game type is determined later based on user input,
        so it's not passed during initialization.
        """
        # self.game_type will be set based on user choice in __main__
        self.game_type: str = ''
        self.board: list[str] = [' ' for _ in range(10)]
        self.current_turn: str = 'X'
        self.user_symbol: str = '' # To store the user's chosen symbol in computer mode
        self.computer_symbol: str = '' # To store the computer's symbol in computer mode

    def display_board(self) -> None:
        """
        Prints the current state of the Tic-Tac-Toe board to the console.
        """
        print(f"""
        {self.board[1]}  |  {self.board[2]}  |  {self.board[3]}
        -------------
        {self.board[4]}  |  {self.board[5]}  |  {self.board[6]}
        -------------
        {self.board[7]}  |  {self.board[8]}  |  {self.board[9]}
        """)

    def make_move(self, position: int) -> bool:
        """
        Attempts to make a move on the board at the given position for the current player.

        :param position: The position on the board (1-9) where the player wants to move.
        :type position: int
        :returns: True if the move was successful, False otherwise (invalid position or already taken).
        :rtype: bool
        """
        if not (1 <= position <= 9):
            print("Invalid move. Position must be between 1 and 9. Try again.")
            return False
        if self.board[position] == " ":
            self.board[position] = self.current_turn
            return True
        else:
            print("Invalid move. That position is already taken. Try again.")
            return False

    def switch_turn(self) -> None:
        """
        Switches the current player's turn from 'X' to 'O' or 'O' to 'X'.
        """
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'

    def check_winner(self) -> bool:
        """
        Checks if the current player has won the game.

        :returns: True if there's a winner, False otherwise.
        :rtype: bool
        """
        winning_combinations: list[tuple[int, int, int]] = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
            (1, 5, 9), (3, 5, 7)              # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def is_board_full(self) -> bool:
        """
        Checks if the Tic-Tac-Toe board is completely full.

        :returns: True if the board is full, False otherwise.
        :rtype: bool
        """
        return " " not in self.board[1:]

    def random_move(self) -> bool:
        """
        Makes a random move for the computer on an available position.

        :returns: True if a move was made, False if no available positions.
        :rtype: bool
        """
        available_positions: list[int] = [i for i in range(1, 10) if self.board[i] == " "]
        if available_positions:
            position: int = random.choice(available_positions)
            self.board[position] = self.current_turn
            return True
        return False

    def start_game_with_computer(self) -> None:
        """
        Starts and manages a Tic-Tac-Toe game against the computer.
        """
        self.display_board()
        self.user_symbol = input("Choose your symbol (X or O): ").upper()
        while self.user_symbol not in ['X', 'O']:
            print("Invalid choice. Please choose 'X' or 'O'.")
            self.user_symbol = input("Choose your symbol (X or O): ").upper()

        self.computer_symbol = 'O' if self.user_symbol == 'X' else 'X'

        while True:
            if self.current_turn == self.user_symbol:
                while True:
                    try:
                        position: int = int(input(f"Your turn ({self.user_symbol}). Enter your move (1-9): "))
                        if self.make_move(position):
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 9.")
                self.display_board()
            else: # Computer's turn
                print("Computer's turn...")
                # The computer's move will always be valid, so no need for a loop here
                self.random_move()
                self.display_board()

            if self.check_winner():
                if self.current_turn == self.user_symbol:
                    print(f"Congratulations! You won!")
                else:
                    print("Computer won!")
                break
            if self.is_board_full():
                print("It's a draw!")
                break

            self.switch_turn()

    def start_game_with_friend(self) -> None:
        """
        Starts and manages a Tic-Tac-Toe game between two players.
        """
        self.display_board()
        first_player: str = input("Enter the first player name who will play with X: ")
        second_player: str = input("Enter the second player name who will play with O: ")

        while True:
            current_player_name: str = first_player if self.current_turn == 'X' else second_player
            current_player_symbol: str = self.current_turn

            while True:
                try:
                    position: int = int(input(f"{current_player_name}'s turn ({current_player_symbol}). Enter your move (1-9): "))
                    if self.make_move(position):
                        break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")

            self.display_board()
            if self.check_winner():
                print(f"Congratulations, {current_player_name} won!")
                break
            if self.is_board_full():
                print("It's a draw!")
                break

            self.switch_turn()


if __name__ == "__main__":
    game: TicTacToe = TicTacToe()
    while True:
        game_type_choice: str = input(f"""
                Welcome to the Tic Tac Toe game.
                Choose how do you want to play the game?
                1 - To play with computer.
                2 - To play with your friend.
                """)
        if game_type_choice == '1':
            game.game_type = 'with_computer' # Set game_type after user choice
            game.start_game_with_computer()
            break
        elif game_type_choice == '2':
            game.game_type = 'with_friend' # Set game_type after user choice
            game.start_game_with_friend()
            break
        else:
            print("Wrong choice. Choose between 1 or 2.")
            continue