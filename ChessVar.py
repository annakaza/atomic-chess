# Project: Atomic Chess
# Author: Anna Kaza

# This project is an implementation of Atomic Chess using object-oriented programming in Python.

# Each chess piece is represented as a class, with movement logic based on standard chess rules and modified
# according to Atomic Chess rules (e.g., explosions on capture).
# Subclasses like Pawn, Rook, Knight, Bishop, Queen, and King inherit from a shared superclass, Piece.
# The main class, ChessVar, manages the board state, validates moves, enforces Atomic Chess rules,
# tracks the game state (whose turn it is or if the game is won), and prints the board in a readable format.

# This project demonstrates class inheritance, rule-based game logic, algebraic notation parsing,
# and interaction between multiple objects to model a complex board game.

class Piece:
    """
    Represents a generic chess piece with a color ('w' for white or 'b' for black).
    Superclass for Pawn, Rook, Knight, Bishop, Queen, and King.
    """
    def __init__(self, color):
        """Initialize a piece with the given color."""
        self._color = color

    def get_color(self):
        """Return the color of the piece ('w' or 'b')."""
        return self._color


class Pawn(Piece):
    """
    Represents a pawn chess piece.
    Inherits from Piece and provides pawn-specific movement validation and symbol.
    """
    def __init__(self, color):
        """Initialize a pawn with the given color and corresponding symbol ('P_w' for white or 'P_b' for black)."""
        super().__init__(color)
        self._symbol = 'P_' + self._color

    def get_symbol(self):
        """Return the pawn's symbol."""
        return self._symbol

    def is_move_valid(self, row_from, column_from, row_to, column_to, square_to, board):
        """
        Check if a given move is valid for the pawn.

        Parameters:
            - row_from (int): row from which the pawn is moved
            - column_from (int): column from which the pawn is moved
            - row_to (int): row to which the pawn is moved
            - column_to (int): column to which the pawn is moved
            - square_to (Piece object or None): object at the square to which the pawn is moved
            - board (list): the current state of the board (containing Piece objects or None)

        Returns:
            - True if the given move is valid
            - False otherwise
        """
        # validate a pawn's forward move with no capture (allowing to move two squares on its first move)
        if square_to is None and column_from == column_to:
            if self._color == "w":
                if row_from == 6 and row_from - row_to == 2 and board[row_from - 1][column_from] is None:
                    return True
                if row_from - row_to == 1:
                    return True
            if self._color == "b":
                if row_from == 1 and row_to - row_from == 2 and board[row_from + 1][column_from] is None:
                    return True
                if row_to - row_from == 1:
                    return True

        # validate a pawn's diagonal move with a capture
        if square_to is not None and abs(column_from - column_to) == 1:
            if self._color == 'w' and row_from - row_to == 1:
                return True
            if self._color == 'b' and row_to - row_from == 1:
                return True

        # move is not valid
        return False


class Rook(Piece):
    """
    Represents a rook chess piece.
    Inherits from Piece and provides rook-specific movement validation and symbol.
    """
    def __init__(self, color):
        """Initialize a rook with the given color and corresponding symbol ('R_w' for white or 'R_b' for black)."""
        super().__init__(color)
        self._symbol = 'R_' + self._color

    def get_symbol(self):
        """Return the rook's symbol."""
        return self._symbol

    def is_move_valid(self, row_from, column_from, row_to, column_to, square_to, board):
        """
        Check if a given move is valid for the rook.

        Parameters:
            - row_from (int): row from which the rook is moved
            - column_from (int): column from which the rook is moved
            - row_to (int): row to which the rook is moved
            - column_to (int): column to which the rook is moved
            - square_to (Piece object or None): object at the square to which the rook is moved
            - board (list): the current state of the board (containing Piece objects or None)

        Returns:
            - True if the given move is valid
            - False otherwise
        """
        # validate a rook's vertical move
        if column_from == column_to:
            if row_from < row_to:
                step = 1
            else:
                step = -1
            for row in range(row_from + step, row_to, step):
                if board[row][column_from] is not None:
                    return False
            return True

        # validate a rook's horizontal move
        if row_from == row_to:
            if column_from < column_to:
                step = 1
            else:
                step = -1
            for column in range(column_from + step, column_to, step):
                if board[row_from][column] is not None:
                    return False
            return True

        # move is not valid
        return False


class Knight(Piece):
    """
    Represents a knight chess piece.
    Inherits from Piece and provides knight-specific movement validation and symbol.
    """
    def __init__(self, color):
        """Initialize a knight with the given color and corresponding symbol ('N_w' for white or 'N_b' for black)."""
        super().__init__(color)
        self._symbol = 'N_' + self._color

    def get_symbol(self):
        """Return the knight's symbol."""
        return self._symbol

    def is_move_valid(self, row_from, column_from, row_to, column_to, square_to, board):
        """
        Check if a given move is valid for the knight.

        Parameters:
            - row_from (int): row from which the knight is moved
            - column_from (int): column from which the knight is moved
            - row_to (int): row to which the knight is moved
            - column_to (int): column to which the knight is moved
            - square_to (Piece object or None): object at the square to which the knight is moved
            - board (list): the current state of the board (containing Piece objects or None)

        Returns:
            - True if the given move is valid
            - False otherwise
        """
        # validate a knight's 2-by-1 L-shape movement
        two_by_one = (abs(column_from - column_to) == 2 and abs(row_from - row_to) == 1)

        # validate a knight's 1-by-2 L-shape movement
        one_by_two = (abs(column_from - column_to) == 1 and abs(row_from - row_to) == 2)

        # move is not valid if both validations are False
        return two_by_one or one_by_two


class Bishop(Piece):
    """
    Represents a bishop chess piece.
    Inherits from Piece and provides bishop-specific movement validation and symbol.
    """
    def __init__(self, color):
        """Initialize a bishop with the given color and corresponding symbol ('B_w' for white or 'B_b' for black)."""
        super().__init__(color)
        self._symbol = 'B_' + self._color

    def get_symbol(self):
        """Return the bishop's symbol."""
        return self._symbol

    def is_move_valid(self, row_from, column_from, row_to, column_to, square_to, board):
        """
        Check if a given move is valid for the bishop.

        Parameters:
            - row_from (int): row from which the bishop is moved
            - column_from (int): column from which the bishop is moved
            - row_to (int): row to which the bishop is moved
            - column_to (int): column to which the bishop is moved
            - square_to (Piece object or None): element at the square to which the bishop is moved
            - board (list): the current state of the board (containing Piece objects or None)

        Returns:
            - True if the given move is valid
            - False otherwise
        """
        # validate if bishop moved diagonally
        if abs(column_from - column_to) != abs(row_from - row_to):
            return False

        # validate if diagonal path is not blocked by other pieces
        if row_from < row_to:
            row_step = 1
        else:
            row_step = -1
        if column_from < column_to:
            col_step = 1
        else:
            col_step = -1
        next_row = row_from + row_step
        next_column = column_from + col_step
        while next_row != row_to and next_column != column_to:
            if board[next_row][next_column] is not None:
                return False
            next_row += row_step
            next_column += col_step

        # move is valid
        return True


class Queen(Piece):
    """
    Represents a queen chess piece.
    Inherits from Piece and provides queen-specific movement validation and symbol.
    """
    def __init__(self, color):
        """Initialize a queen with the given color and corresponding symbol ('Q_w' for white or 'Q_b' for black)."""
        super().__init__(color)
        self._symbol = 'Q_' + self._color
        self._rook_movement = Rook(color)       # delegate horizontal/vertical validation
        self._bishop_movement = Bishop(color)   # delegate diagonal validation

    def get_symbol(self):
        """Return the queen's symbol."""
        return self._symbol

    def is_move_valid(self, row_from, column_from, row_to, column_to, square_to, board):
        """
        Check if a given move is valid for the queen.
        Since queens combine movement abilities of rooks and bishops, validation is delegated to both movement types.

        Parameters:
            - row_from (int): row from which the queen is moved
            - column_from (int): column from which the queen is moved
            - row_to (int): row to which the queen is moved
            - column_to (int): column to which the queen is moved
            - square_to (Piece object or None): element at the square to which the queen is moved
            - board (list): the current state of the board (containing Piece objects or None)

        Returns:
            - True if the given move is valid
            - False otherwise
        """
        # check if queen made a valid horizontal/vertical move
        rook_move = self._rook_movement.is_move_valid(row_from, column_from, row_to, column_to, square_to, board)

        # check if queen made a valid diagonal move
        bishop_move = self._bishop_movement.is_move_valid(row_from, column_from, row_to, column_to, square_to, board)

        # move is not valid if both validations are False
        return rook_move or bishop_move


class King(Piece):
    """
    Represents a king chess piece.
    Inherits from Piece and provides king-specific movement validation and symbol.
    """
    def __init__(self, color):
        """Initialize a king with the given color and corresponding symbol ('K_w' for white or 'K_b' for black)."""
        super().__init__(color)
        self._symbol = 'K_' + self._color

    def get_symbol(self):
        """Return the king's symbol."""
        return self._symbol

    def is_move_valid(self, row_from, column_from, row_to, column_to, square_to, board):
        """
        Check if a given move is valid for the king. In Atomic Chess, kings cannot capture.

        Parameters:
            - row_from (int): row from which the king is moved
            - column_from (int): column from which the king is moved
            - row_to (int): row to which the king is moved
            - column_to (int): column to which the king is moved
            - square_to (Piece object or None): element at the square to which the king is moved
            - board (list): the current state of the board (containing Piece objects or None)

        Returns:
            - True if the given move is valid
            - False otherwise
        """
        # validate if king moved one square in any direction and did NOT make a capture
        # move is not valid if any validation is False
        return (square_to is None) and (0 <= abs(row_from - row_to) <= 1) and (0 <= abs(column_from - column_to) <= 1)


class ChessVar:
    """
    Represents a game of Atomic Chess.

    Sets up the board, enforces Atomic Chess rules, validates moves,
    tracks turn order and game state, and provides board display.
    """
    def __init__(self):
        """Initialize the chessboard, game state, and turn tracker."""
        # The chessboard is a 8x8 list of lists.
        # Index 0 (top) is row 8, and index 7 (bottom) is row 1 (in chess notation).
        # Inner list indices 0–7 represent columns 'a' through 'h' (in chess notation).
        self._board = [
            [Rook('b'), Knight('b'), Bishop('b'), Queen('b'), King('b'), Bishop('b'), Knight('b'), Rook('b')],
            [Pawn('b')] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [Pawn('w')] * 8,
            [Rook('w'), Knight('w'), Bishop('w'), Queen('w'), King('w'), Bishop('w'), Knight('w'), Rook('w')],
        ]
        self._game_state = 'UNFINISHED'     # can be 'UNFINISHED','WHITE WON', or 'BLACK WON'
        self._turn = 'w'                    # can be 'w' for white or 'b' for black

    def get_game_state(self):
        """Return the current game state ('UNFINISHED', 'WHITE WON', or 'BLACK WON')"""
        return self._game_state

    def make_move(self, string_from, string_to):
        """
        Attempt to make a move from one square to another using algebraic notation:
            - validate game state, turn, move legality, and game rules
            - Apply capture explosion if applicable
            - Update board, turn, and game state (if applicable)
            - End game if a king is captured via explosion

        Parameters:
            - string_from: a string that represents the square moved from
            - string_to: a string that represents the square moved to

        Returns:
            - True if the given move was valid and executed
            - False otherwise
        """
        # check if game was already won
        if self._game_state != 'UNFINISHED':
            return False

        # check if piece is being moved to its current square
        if string_from == string_to:
            return False

        # convert string_from and string_to from algebraic notation into row and column indices of self._board
        row_from = 8 - int(string_from[1])
        column_from = ord(string_from[0]) - ord('a')
        row_to = 8 - int(string_to[1])
        column_to = ord(string_to[0]) - ord('a')

        # object (Piece object or None) at the square FROM which a piece is moved
        square_from = self._board[row_from][column_from]
        # object (Piece object or None) at the square TO which a piece is moved
        square_to = self._board[row_to][column_to]

        # check if the square being moved FROM is empty or contains the opponent's piece
        if square_from is None or square_from.get_color() != self._turn:
            return False

        # check if a piece is being moved TO a square outside the board
        if not (0 <= column_to <= 7 and 0 <= row_to <= 7):
            return False

        # check if the square being moved TO contains the player's own piece
        if square_to is not None and square_to.get_color() == self._turn:
            return False

        # check if the move is valid in terms of piece-specific rules
        if square_from.is_move_valid(row_from, column_from, row_to, column_to, square_to, self._board):

            # if move is valid and no capture occurs, execute move by updating the board and turn
            if square_to is None:
                self._board[row_from][column_from] = None
                self._board[row_to][column_to] = square_from
                self.change_turn()

            # if move is valid and a capture occurs, validate further
            else:
                # if the player's own king will explode, move is not valid and not executed
                if self.is_own_king_exploded(row_to, column_to):
                    return False

                # execute move by updating the board
                self._board[row_from][column_from] = None

                # if the opponent's king is exploded, update the game state
                if self.is_opponent_king_exploded(row_to, column_to):
                    if self._turn == 'w':
                        self._game_state = 'WHITE WON'
                    else:
                        self._game_state = 'BLACK WON'
                # if not, update the turn
                else:
                    self.change_turn()

                # execute the explosion
                self.execute_explosion(row_to, column_to)

            # move was valid and executed
            return True

        # move was not executed
        return False

    def change_turn(self):
        """Switch to the other player's turn."""
        if self._turn == 'w':
            self._turn = 'b'
        else:
            self._turn = 'w'

    def is_own_king_exploded(self, row_to, column_to):
        """
        Check if the player's own king will be caught in the explosion from the attempted capture.

        Parameters:
            - row_to (int): row to which the piece is moved
            - column_to (int): column to which the piece is moved

        Returns:
            - True if the player's own king will explode
            - False otherwise
        """
        for row in range(max(row_to - 1, 0), min(row_to + 2, 8)):
            for column in range(max(column_to - 1, 0), min(column_to + 2, 8)):
                piece = self._board[row][column]
                if piece is not None and piece.get_symbol()[0] == 'K':
                    if piece.get_color() == self._turn:
                        return True
        return False

    def is_opponent_king_exploded(self, row_to, column_to):
        """
        Check if the opponent's king will be caught in the explosion from the performed capture.

        Parameters:
            - row_to (int): row to which the piece is moved
            - column_to (int): column to which the piece is moved

        Returns:
            - True if the opponent's king will explode
            - False otherwise
        """
        for row in range(max(row_to - 1, 0), min(row_to + 2, 8)):
            for column in range(max(column_to - 1, 0), min(column_to + 2, 8)):
                piece = self._board[row][column]
                if piece is not None and piece.get_symbol()[0] == 'K':
                    if piece.get_color() != self._turn:
                        return True
        return False

    def execute_explosion(self, row_to, column_to):
        """
        Apply Atomic Chess explosion rules at the square of capture.
        Removes the captured piece, the capturing piece, and all adjacent non-pawn pieces.
        Pawns are only exploded when captured directly.

        Parameters:
            - row_to (int): row to which the piece is moved
            - column_to (int): column to which the piece is moved
        """
        for row in range(max(row_to - 1, 0), min(row_to + 2, 8)):
            for column in range(max(column_to - 1, 0), min(column_to + 2, 8)):
                piece = self._board[row][column]
                if piece is not None and not (piece.get_symbol()[0] == 'P' and (row != row_to or column != column_to)):
                    self._board[row][column] = None

    def print_board(self):
        """Print the current state of the board."""
        for row in range(8):
            print(8 - row, end='  ')
            for square in self._board[row]:
                if square is None:
                    print(' . ', end='  ')
                else:
                    print(square.get_symbol(), end='  ')
            print()
        print('    a    b    c    d    e   f    g    h')
