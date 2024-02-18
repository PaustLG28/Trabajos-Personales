import os
import sys
import random
import threading
import multiprocessing
import time

# Constantes
EMPTY = "-"
PLAYER_X = "X"
PLAYER_O = "O"
BOARD_SIZE = 3

# Clase para representar el tablero del juego
class Board:
    def __init__(self):
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.lock = threading.Lock()

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def check_winner(self):
        # Comprobar filas
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != EMPTY:
                return True

        # Comprobar columnas
        for col in range(BOARD_SIZE):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != EMPTY:
                return True

        # Comprobar diagonales
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return True

        return False

    def make_move(self, row, col, player):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = player
            return True
        return False

# Función para que un jugador realice su movimiento
def player_move(board, player):
    while True:
        try:
            row = int(input("Fila (1-3): ")) - 1
            col = int(input("Columna (1-3): ")) - 1
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                with board.lock:
                    if board.make_move(row, col, player):
                        break
                    else:
                        print("Esa casilla ya está ocupada. Intenta nuevamente.")
            else:
                print("Movimiento inválido. Introduce números entre 1 y 3.")
        except ValueError:
            print("Entrada inválida. Introduce números.")

# Función para que la IA realice su movimiento
def ai_move(board, player):
    while True:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        with board.lock:
            if board.make_move(row, col, player):
                break

# Función para ejecutar el juego
def play_game():
    board = Board()
    board.print_board()

    players = [PLAYER_X, PLAYER_O]
    current_player = random.choice(players)

    while True:
        if current_player == PLAYER_X:
            print("Turno de X:")
            player_move(board, PLAYER_X)
        else:
            print("Turno de O (IA):")
            ai_move(board, PLAYER_O)

        board.print_board()

        if board.check_winner():
            print(f"¡{current_player} ha ganado!")
            break

        # Cambiar el jugador
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

# Función principal
def main():
    processes = []

    # Crear procesos para ejecutar el juego
    for _ in range(5):
        p = multiprocessing.Process(target=play_game)
        processes.append(p)
        p.start()

    # Esperar a que los procesos terminen
    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
