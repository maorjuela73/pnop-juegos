import random

# Definimos la clase Game
class Game:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.guess = None

    def play(self):
        print("¡Bienvenido al juego de adivinanza!")
        while self.guess != self.secret_number:
            self.get_guess()
            self.attempts += 1
            self.check_guess()

        print(f"¡Felicidades! Adivinaste el número {self.secret_number} en {self.attempts} intentos.")

    def get_guess(self):
        self.guess = int(input("Adivina el número secreto (entre 1 y 100): "))

    def check_guess(self):
        if self.guess < self.secret_number:
            print("El número secreto es mayor. ¡Inténtalo de nuevo!")
        elif self.guess > self.secret_number:
            print("El número secreto es menor. ¡Inténtalo de nuevo!")

# Creamos una instancia del juego y lo iniciamos
if __name__ == "__main__":
    game = Game()
    game.play()
