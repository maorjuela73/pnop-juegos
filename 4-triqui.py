class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Crear un tablero vacío de 3x3
        self.current_player = "X"

    def print_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 9)

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("¡Esa casilla ya está ocupada! Elige otra.")

    def check_winner(self):
        # Comprobar filas, columnas y diagonales para determinar al ganador
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True
        return False

    def check_draw(self):
        return " " not in self.board

    def play(self):
        print("¡Bienvenido al juego de Tres en Línea!")

        while True:
            self.print_board()
            position = int(input(f"Turno del jugador {self.current_player}. Elige una casilla (0-8): "))

            if position < 0 or position > 8:
                print("Selección inválida. Elige un número entre 0 y 8.")
                continue

            self.make_move(position)

            if self.check_winner():
                self.print_board()
                print(f"¡El jugador {self.current_player} ha ganado!")
                break

            if self.check_draw():
                self.print_board()
                print("¡Es un empate!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
