
# Prompt: You are building a GUI based chess game between two players. You are responsible for implementing the following backend API which the front end can call:
# Function 1 (Initialization):
# Input: None
# Output: Error or success
# Function 2 (provide the state of the board): 
# Input: None
# Output: A list of all the available pieces on the board and their locations
# Function 3 (given a move, determine if can be performed and if it can be then perform the move):
# Input: A pieces, it’s starting location and ending location
# Output:
# Either an invalid error (with reason)
# Or return valid move
# Chess description
# Chess is a game played between two players: black and white on a 8x8 board
# Each player has the following pieces:
# 8 Knights
# 8 pawns
# Each piece has a particular way that it can move
# Knight: Do a as many as needed forwad/backward/left/right step. 
# Pawn: Can move 1 step forward and 1 step sideways to remove piece from other team


from typing import List, Tuple

class Piece:
    def __init__(self, piece_type: str, color: str):
        if piece_type not in ["Knight", "Pawn"]:
            raise ValueError("Invalid piece type. Only Knight and Pawn are allowed.")
        if color not in ["White", "Black"]:
            raise ValueError("Color must be either 'White' or 'Black'")
        
        self.piece_type = piece_type
        self.color = color

    def __repr__(self):
        return f"{self.color[0]}{self.piece_type[0]}"  # e.g. "WK" for White Knight


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()

    def initialize_board(self):
        # White pieces
        self.board[6] = [Piece("Pawn", "White") for _ in range(8)]
        self.board[7][1] = Piece("Knight", "White")
        self.board[7][6] = Piece("Knight", "White")

        # Black pieces
        self.board[1] = [Piece("Pawn", "Black") for _ in range(8)]
        self.board[0][1] = Piece("Knight", "Black")
        self.board[0][6] = Piece("Knight", "Black")

    def get_board_state(self) -> List[Tuple[str, str, Tuple[int, int]]]:
        state = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    state.append((piece.color, piece.piece_type, (row, col)))
        return state

    def is_valid_move(self, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        sx, sy = start
        ex, ey = end

        if not (0 <= sx < 8 and 0 <= sy < 8 and 0 <= ex < 8 and 0 <= ey < 8):
            return False

        piece = self.board[sx][sy]
        if piece is None:
            return False

        target = self.board[ex][ey]
        if target and target.color == piece.color:
            return False  # Can't capture own piece

        dx, dy = ex - sx, ey - sy

        if piece.piece_type == "Knight":
            return (abs(dx), abs(dy)) in [(2, 1), (1, 2)]

        elif piece.piece_type == "Pawn":
            direction = -1 if piece.color == "White" else 1
            # Move forward
            if dx == direction and dy == 0 and target is None:
                return True
            # Capture diagonally
            if dx == direction and abs(dy) == 1 and target and target.color != piece.color:
                return True

        return False

    def move_piece(self, start: Tuple[int, int], end: Tuple[int, int]) -> str:
        if self.is_valid_move(start, end):
            sx, sy = start
            ex, ey = end
            self.board[ex][ey] = self.board[sx][sy]
            self.board[sx][sy] = None
            return "Move performed"
        else:
            return "Invalid move"

# Example usage
if __name__ == "__main__":
    board = ChessBoard()
    print("Initial Board State:")
    for item in board.get_board_state():
        print(item)

    print(board.move_piece((6, 0), (5, 0)))  # Valid pawn move
    print(board.move_piece((7, 1), (5, 2)))  # Valid knight move
    print(board.move_piece((6, 1), (4, 1)))  # Invalid pawn move (2 squares forward)
