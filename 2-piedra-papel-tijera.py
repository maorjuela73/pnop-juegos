import random

# Definimos la clase Game
class RockPaperScissors:
    def __init__(self):
        self.choices = ["Piedra", "Papel", "Tijeras"]
        self.player_score = 0
        self.computer_score = 0

    def play(self):
        print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")

        while True:
            player_choice = self.get_player_choice()
            computer_choice = random.choice(self.choices)

            print(f"Tú elegiste: {player_choice}")
            print(f"La computadora eligió: {computer_choice}")

            if player_choice == computer_choice:
                print("¡Empate!")
            elif (
                (player_choice == "Piedra" and computer_choice == "Tijeras") or
                (player_choice == "Papel" and computer_choice == "Piedra") or
                (player_choice == "Tijeras" and computer_choice == "Papel")
            ):
                print("¡Tú ganas!")
                self.player_score += 1
            else:
                print("La computadora gana.")
                self.computer_score += 1

            print(f"Puntuación - Tú: {self.player_score}, Computadora: {self.computer_score}")

            play_again = input("¿Quieres jugar de nuevo? (s/n): ")
            if play_again.lower() != "s":
                break

        print("¡Gracias por jugar!")

    def get_player_choice(self):
        while True:
            player_choice = input("Elige Piedra, Papel o Tijeras: ")
            if player_choice in self.choices:
                return player_choice
            else:
                print("Selección no válida. Por favor, elige nuevamente.")

# Creamos una instancia del juego y lo iniciamos
if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()
