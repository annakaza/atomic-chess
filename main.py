# Command-line interface for playing Atomic Chess.
# Run this file to play interactively in the terminal.
# White moves first.

from ChessVar import ChessVar

def main():
    print("Welcome to Atomic Chess!\n")
    print("Please enter your moves using algebraic notation.")
    print("For example, 'd1' corresponds to the square with the white queen (Q_w).\n")
    print("White moves first.\n")

    game = ChessVar()

    while game.get_game_state() == 'UNFINISHED':
        game.print_board()
        
        move_from = input("Move from: ").strip().lower()    #correct accidental spaces or capitalization
        move_to = input("Move to: ").strip().lower()
        
        if not game.make_move(move_from, move_to):
            print("Invalid move. Try again.")

    game.print_board()
    print(f"Game over: {game.get_game_state()}!")

if __name__ == "__main__":
    main()
