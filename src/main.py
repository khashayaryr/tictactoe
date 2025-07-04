import random

class TicTacToe:
    def __init__(self, game_type='with_computer'):
        self.game_type = game_type
        self.board = [' ' for _ in range(10)]
        self.current_turn = 'X'

    def display_board(self):
        print(f"""
        {self.board[1]}  |  {self.board[2]}  |  {self.board[3]}
        -------------
        {self.board[4]}  |  {self.board[5]}  |  {self.board[6]}
        -------------
        {self.board[7]}  |  {self.board[8]}  |  {self.board[9]}
        """)

    def make_move(self, position):
        # Add a check for valid position range (1-9)
        if not (1 <= position <= 9):
            print("Invalid move. Position must be between 1 and 9. Try again.")
            return False
        if self.board[position] == " ":
            self.board[position] = self.current_turn
            return True
        else:
            print("Invalid move. That position is already taken. Try again.")
            return False

    def switch_turn(self):
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
            (1, 5, 9), (3, 5, 7)              # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def is_board_full(self):
        return " " not in self.board[1:]

    def random_move(self):
        available_positions = [i for i in range(1, 10) if self.board[i] == " "]
        if available_positions:
            position = random.choice(available_positions)
            self.board[position] = self.current_turn
            return True
        return False

    def start_game_with_computer(self):
        self.display_board()
        self.user_symbol = input("Choose your symbol (X or O): ").upper()
        while self.user_symbol not in ['X', 'O']: # Loop until valid symbol is chosen
            print("Invalid choice. Please choose 'X' or 'O'.")
            self.user_symbol = input("Choose your symbol (X or O): ").upper()

        self.computer_symbol = 'O' if self.user_symbol == 'X' else 'X'
        self.current_turn = 'X' # Always start with X

        while True:
            if self.current_turn == self.user_symbol:
                while True: # Loop for user's turn until valid move
                    try:
                        position = int(input(f"Your turn ({self.user_symbol}). Enter your move (1-9): "))
                        if self.make_move(position):
                            break # Exit the loop if move is valid
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 9.")
                self.display_board()
            else: # Computer's turn
                print("Computer's turn...")
                self.random_move()
                self.display_board() # Display board after computer's move

            if self.check_winner():
                if self.current_turn == self.user_symbol:
                    print(f"Congratulations! You won!")
                else:
                    print("Computer won!")
                break
            if self.is_board_full():
                print("It's a draw!")
                break

            self.switch_turn() # Switch turn only after a valid move or computer's move

    def start_game_with_friend(self):
        self.display_board()
        first_player = input("Enter the first player name who will play with X: ")
        second_player = input("Enter the second player name who will play with O: ")
        self.current_turn = 'X' # Always start with X

        while True:
            current_player_name = first_player if self.current_turn == 'X' else second_player
            current_player_symbol = self.current_turn

            while True: # Loop for current player's turn until valid move
                try:
                    position = int(input(f"{current_player_name}'s turn ({current_player_symbol}). Enter your move (1-9): "))
                    if self.make_move(position):
                        break # Exit the loop if move is valid
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")

            self.display_board()
            if self.check_winner():
                print(f"Congratulations, {current_player_name} won!")
                break
            if self.is_board_full():
                print("It's a draw!")
                break

            self.switch_turn() # Switch turn only after a valid move


if __name__ == "__main__":
    game = TicTacToe()
    while True:
        game_type = input(f"""
                Welcome to the Tic Tac Toe game.
                Choose how do you want to play the game?
                1 - To play with computer.
                2 - To play with your friend.
                """)
        if game_type == '1':
            game.start_game_with_computer()
            break
        elif game_type == '2':
            game.start_game_with_friend()
            break
        else:
            print("Wrong choice. Choose between 1 or 2.")
            continue