class Piece:
    def __init__(self, name, color):
        self.name = name  # p.ej. 'Pawn', 'King', etc.
        self.color = color  # 'white' o 'black'

    def __repr__(self):
        return f'{self.name[0]}{self.color[0]}'

class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Crea un tablero vacío de 8x8
        board = [[None for _ in range(8)] for _ in range(8)]

        # Coloca las piezas blancas
        board[0] = [
            Piece('Rook', 'white'), Piece('Knight', 'white'), Piece('Bishop', 'white'), Piece('Queen', 'white'),
            Piece('King', 'white'), Piece('Bishop', 'white'), Piece('Knight', 'white'), Piece('Rook', 'white')
        ]
        board[1] = [Piece('Pawn', 'white') for _ in range(8)]

        # Coloca las piezas negras
        board[7] = [
            Piece('Rook', 'black'), Piece('Knight', 'black'), Piece('Bishop', 'black'), Piece('Queen', 'black'),
            Piece('King', 'black'), Piece('Bishop', 'black'), Piece('Knight', 'black'), Piece('Rook', 'black')
        ]
        board[6] = [Piece('Pawn', 'black') for _ in range(8)]

        return board

    def print_board(self):
        print("  a b c d e f g h")
        print("  ----------------")
        for i, row in enumerate(self.board):
            row_str = f'{8 - i} '
            for piece in row:
                row_str += f'{piece if piece else "."} '
            print(row_str + f'{8 - i}')
        print("  ----------------")
        print("  a b c d e f g h")

    def move_piece(self, start, end):
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')
        
        piece = self.board[start_row][start_col]
        
        if not piece:
            print("No hay pieza en esa posición.")
            return False
        
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = None
        return True

def play_game():
    board = Board()
    turn = 'white'

    while True:
        board.print_board()
        print(f"Turno de {turn}")
        start = input("Mover desde (ej: e2): ")
        end = input("Mover hacia (ej: e4): ")
        
        if board.move_piece(start, end):
            turn = 'black' if turn == 'white' else 'white'
        else:
            print("Movimiento inválido, intenta nuevamente.")

if __name__ == "__main__":
    play_game()
