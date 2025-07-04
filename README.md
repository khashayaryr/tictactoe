# Tic-Tac-Toe Game

A simple and interactive Tic-Tac-Toe game implemented in Python. Play against a computer opponent or challenge a friend in a local multiplayer mode!

## Table of Contents

* [Features](#features)
* [How to Play](#how-to-play)
* [Board Layout](#board-layout)
* [Installation](#installation)
* [Usage](#usage)
* [Code Structure](#code-structure)
* [Contributing](#contributing)
* [License](#license)

## Features

* **Two Game Modes:**
    * **Player vs. Computer:** Test your skills against a random-move AI.
    * **Player vs. Player:** Play with a friend on the same computer.
* **Interactive Command-Line Interface:** Clear board display and user-friendly prompts.
* **Input Validation:** Handles invalid moves (e.g., out-of-range numbers, already taken positions) gracefully.
* **Clear Game Outcomes:** Announces wins, losses, or draws.
* **Pythonic Design:** Utilizes a class-based structure for better organization and reusability.
* **Type Hinting & Docstrings:** Code is well-documented with type annotations and reStructuredText-style docstrings for improved readability and maintainability.

## How to Play

Tic-Tac-Toe is a classic two-player game played on a 3x3 grid.
* Players take turns marking a square with their symbol (X or O).
* The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
* If all nine squares are filled and no player has three marks in a row, the game is a draw.

## Board Layout

The Tic-Tac-Toe board uses numbers 1 through 9 to represent each position. When prompted to make a move, you should enter the number corresponding to the square where you want to place your 'X' or 'O'.

Here's how the numbers map to the board:
```
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
```

## Installation

This game requires Python 3.x.

1.  **Clone the repository (or download the script):**

    ```bash
    git clone https://github.com/khashayaryr/tictactoe.git
    cd tictactoe
    ```

2.  **No additional libraries are required**, as it only uses the built-in `random` module.

## Usage

To run the game:

- Navigate to the project's root directory in your terminal (`tictactoe`).
- Add the current directory to your `PYTHONPATH` to ensure Python can find the `src` module and run the main script:

    ```bash
    export PYTHONPATH=$PYTHONPATH:$(pwd)
    python src/main.py
    ```

- Follow the on-screen prompts to choose your game mode and make your moves.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

---
**Enjoy the game!**
