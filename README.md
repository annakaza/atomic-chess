# Atomic Chess

A Python implementation of Atomic Chess - a variant of standard chess where all captures trigger an explosion. This project was built using **object-oriented programming** principles and is playable in the terminal via a command-line interface.

---

## What Is Atomic Chess?

Atomic Chess modifies the rules of classical chess by adding explosions:

- When a piece is captured, all adjacent **non-pawn** pieces, including the capturing piece, are also removed from the board.
- **Pawns** are only removed if directly captured.
- **Kings** cannot capture and cannot be destroyed in a mutual explosion.
- The game ends when a king is destroyed by an explosion.

---

## Features

- Full 8x8 chessboard setup and display
- Class-based design for all piece types
- Piece-specific move validation
- Algebraic notation input (e.g., `e2`, `g5`)
- Explosions remove surrounding non-pawn pieces after a capture
- Win detection when a king is destroyed
- Interactive terminal-based gameplay with real-time board rendering

---

## How to Play

1. Clone this repo or download `ChessVar.py` and `main.py`.
2. Run the game in your terminal:

```bash
python main.py
```

3. Enter moves in algebraic notation:

```
Move from: e2
Move to: e4
```

- White goes first
- The game ends when a king is exploded

---

## Project Structure

- `ChessVar.py` — main game logic, including piece classes and board management
- `main.py` — simple terminal interface for interactive play

---

## Concepts Demonstrated

- Object-oriented design with class inheritance
- Game state management
- Move validation and board representation
- Explosion mechanics and conditional logic
- String parsing for algebraic notation

---

## Author

Created by Anna Kaza

---

## Board Layout (Algebraic Notation)

![chessboard](starting_position.png "starting position")