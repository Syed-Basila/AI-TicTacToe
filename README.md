# AI-TicTacToe
## Project Description
This project is a classic Tic-Tac-Toe game implemented in Python using the Tkinter library for the graphical user interface (GUI). The game features a simple but effective AI opponent using the Minimax algorithm, ensuring that the AI plays optimally.

# Features
Player vs. AI: Play against the computer which uses the Minimax algorithm to make its moves.
Graphical User Interface: An intuitive and easy-to-use GUI built with Tkinter.
Win and Tie Detection: The game correctly identifies win and tie conditions and prompts the user accordingly.
Reset Functionality: The game board resets after a win or a tie, allowing for continuous play.
Demo Video
[Link to Demo Video]

## Installation

## Install dependencies:
pip install tk
Usage
Run the game:
python tictactoe.py
## Code Overview
TicTacToe Class
` Initialization `: Sets up the main game window and initializes the game state.
` create_board `: Creates a 3x3 grid of buttons representing the game board.
` button_click `: Handles player's move, checks for a win/tie, and triggers the AI's move.
` ai_move `: Uses the Minimax algorithm to determine the optimal move for the AI.
` minimax `: Implements the Minimax algorithm to evaluate potential moves.
` check_win `: Checks the current game state for a win condition.
` check_win_static `: Static method for checking win conditions during Minimax evaluation.
` check_tie `: Checks the current game state for a tie condition.
` check_tie_static `: Static method for checking tie conditions during Minimax evaluation.
` reset_board `: Resets the game board for a new game.
## Entry Point
start_game: Initializes the Tkinter root window and starts the main event loop.
## Future Improvements
Add a two-player mode for local multiplayer games.
Implement different difficulty levels for the AI.
Enhance the GUI with better graphics and animations.
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.
