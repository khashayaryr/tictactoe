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
        if self.board[position] == " ":
            self.board[position] = self.current_turn
            return True
        else:
            print("Invalid move. Try again.")
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
        if self.user_symbol not in ['X', 'O']:
            print("Invalid choice.")
            return self.start_game_with_computer()
        while True:
            if self.user_symbol == 'X':
                position = int(input("Enter your move (1-9): "))
                if not self.make_move(position):
                    continue
                self.display_board()
                if self.check_winner():
                    print(f"Congratulation! You won!")
                    break
                if self.is_board_full():
                    print("It's a draw!")
                    break
                self.switch_turn()
                print("Computer's turn...")
                if self.random_move():
                    self.display_board()
                    if self.check_winner():
                        print("Computer won!")
                        break
                    if self.is_board_full():
                        print("It's a draw!")
                        break
                    self.switch_turn()
            else:
                print("Computer's turn...")
                if self.random_move():
                    if self.check_winner():
                        self.display_board()
                        print("Computer won!")
                        break
                    if self.is_board_full():
                        self.display_board()
                        print("It's a draw!")
                        break
                    self.switch_turn()
                self.display_board()
                position = int(input("Enter your move (1-9): "))
                if self.make_move(position):
                    if self.check_winner():
                        self.display_board()
                        print(f"Congratulation! You won!")
                        break
                    if self.is_board_full():
                        self.display_board()
                        print("It's a draw!")
                        break
                    self.switch_turn()


if __name__ == "__main__":
    game = TicTacToe()
    game.start_game_with_computer()
