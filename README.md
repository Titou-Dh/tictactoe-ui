# Strategic Tic Tac Toe with AI

A classic Tic Tac Toe game with a graphical user interface built using Python's Tkinter. This implementation features AI opponents using strategic algorithms.

## Features

- Clean and intuitive graphical interface built with Tkinter
- Play against AI powered by:
  - Minimax algorithm
  - Alpha-Beta pruning optimization
- Clear visual feedback for game progress
- Simple one-click reset functionality

## Project Structure

```
jeu-stratigique/
├── src/
│   ├── main.py         # Application entry point
│   ├── game.py         # Core game logic and board representation
│   ├── gui.py          # Tkinter interface implementation
│   └── ai/
│       ├── __init__.py
│       ├── minmax.py   # Minimax algorithm implementation
│       └── alphabeta.py # Alpha-Beta pruning optimization
├── .gitignore          # Git ignore configuration
├── requirements.txt    # Project dependencies
└── README.md           # This documentation file
```

## How to Play

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the game:
   ```
   python src/main.py
   ```

3. The game interface will appear with a 3×3 grid. Select which AI algorithm you'd like to play against.

4. Click on any empty cell to place your mark (X). The AI (O) will automatically respond with its move.

5. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins the game.

6. If all cells are filled without a winner, the game is declared a draw.

7. Use the "Reset Game" button to start a new game at any time.

## AI Algorithms

### Minimax
The Minimax algorithm works by simulating all possible game states to determine the optimal move. It assumes that both players will play optimally, minimizing potential losses and maximizing potential gains.

### Alpha-Beta Pruning
Alpha-Beta pruning enhances the Minimax algorithm by eliminating branches in the search tree that don't need to be explored, significantly improving performance without affecting the results.

## Requirements

- Python 3.6+
- Tkinter 8.6 (included with most Python installations)
- NumPy

## Future Enhancements

- Adjustable difficulty levels
- Additional AI algorithms
- Game state visualization
- Player statistics tracking
- Custom board sizes

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to submit issues or pull requests.

## License

This project is available as open source under the terms of the MIT License.