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
        # This method uses self.current_turn, which is fine for post-move checks.
        # For AI simulation, we'll use check_winner_for_symbol.
        return self.check_winner_for_symbol(self.current_turn)

    def check_winner_for_symbol(self, symbol: str) -> bool:
        """
        Checks if a given symbol has won the game on the current board state.
        This is primarily used by the AI for simulating moves.

        :param symbol: The symbol ('X' or 'O') to check for a win.
        :type symbol: str
        :returns: True if the given symbol has a winning combination, False otherwise.
        :rtype: bool
        """
        winning_combinations: list[tuple[int, int, int]] = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
            (1, 5, 9), (3, 5, 7)              # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == symbol:
                return True
        return False

    def is_board_full(self) -> bool:
        """
        Checks if the Tic-Tac-Toe board is completely full.

        :returns: True if the board is full, False otherwise.
        :rtype: bool
        """
        return " " not in self.board[1:]

    def get_available_positions(self) -> list[int]:
        """
        Helper method to get a list of all currently available (empty) positions on the board.

        :returns: A list of integers representing available positions (1-9).
        :rtype: list[int]
        """
        return [i for i in range(1, 10) if self.board[i] == " "]

    def calculate_computer_move(self) -> int:
        """
        Calculates the best move for the computer based on the following priority:
        1. Win: If the computer can win in the next move.
        2. Block: If the opponent can win in the next move, block them.
        3. Center: Take the center position if available.
        4. Corners: Take any available corner position.
        5. Sides: Take any available side position.

        :returns: The chosen position for the computer's move.
        :rtype: int
        """
        available_moves: list[int] = self.get_available_positions()

        # 1. Check for computer's winning move
        for move in available_moves:
            self.board[move] = self.computer_symbol # Simulate move
            if self.check_winner_for_symbol(self.computer_symbol):
                self.board[move] = ' ' # Undo simulation
                return move
            self.board[move] = ' ' # Undo simulation

        # 2. Check for opponent's winning move (to block)
        for move in available_moves:
            self.board[move] = self.user_symbol # Simulate opponent's move
            if self.check_winner_for_symbol(self.user_symbol):
                self.board[move] = ' ' # Undo simulation
                return move
            self.board[move] = ' ' # Undo simulation

        # 3. Take the center if available
        if 5 in available_moves:
            return 5

        # 4. Take a corner if available (prioritize randomly among corners if multiple)
        corners: list[int] = [1, 3, 7, 9]
        random.shuffle(corners) # Shuffle to make corner choice less predictable if multiple are open
        for move in corners:
            if move in available_moves:
                return move

        # 5. Take a side if available (prioritize randomly among sides if multiple)
        sides: list[int] = [2, 4, 6, 8]
        random.shuffle(sides) # Shuffle to make side choice less predictable if multiple are open
        for move in sides:
            if move in available_moves:
                return move

        # Fallback: This should ideally not be reached if the board isn't full,
        # but just in case, pick any remaining available move.
        if available_moves:
            return random.choice(available_moves)
        else:
            # This case means the board is full, and a draw or win has occurred already.
            # However, this method is called *before* checking for board full/winner,
            # so it should always find a move if available_moves is not empty.
            raise RuntimeError("No valid moves found, but board is not full.")


    def start_game_with_computer(self) -> None:
        """
        Starts and manages a Tic-Tac-Toe game against the computer.
        """
        self.display_board()
        print("**Remember that in this game, always 'X' will start the game.**")
        self.user_symbol = input("Choose your symbol (X or O): ").upper()
        while self.user_symbol not in ['X', 'O']:
            print("Invalid choice. Please choose 'X' or 'O'.")
            self.user_symbol = input("Choose your symbol (X or O): ").upper()

        self.computer_symbol = 'O' if self.user_symbol == 'X' else 'X'
        self.current_turn = 'X' # Always start with X

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
                # The computer now calculates the best move
                chosen_move: int = self.calculate_computer_move()
                # Make the move using the general make_move method
                self.make_move(chosen_move) # make_move uses self.current_turn, which is correctly set to computer's turn here
                self.display_board()

            # Check for win or draw AFTER each move (player or computer)
            if self.check_winner():
                if self.current_turn == self.user_symbol:
                    print(f"Congratulations! You won!")
                else: # Computer won
                    print("Computer won!")
                break
            if self.is_board_full():
                print("It's a draw!")
                break

            self.switch_turn() # Switch turn only if no winner/draw


    def start_game_with_friend(self) -> None:
        """
        Starts and manages a Tic-Tac-Toe game between two players.
        """
        self.display_board()
        print("**Remember that in this game, always 'X' will start the game.**")
        first_player: str = input("Enter the first player name who will play with X: ")
        second_player: str = input("Enter the second player name who will play with O: ")
        self.current_turn = 'X' # Always start with X

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

                Choose how do you want to play the game:

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
